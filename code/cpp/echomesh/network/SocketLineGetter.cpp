#include "echomesh/network/SocketLineGetter.h"
#include "echomesh/network/LineQueue.h"

namespace echomesh {

namespace {

const bool logAllSocketData = not true;


}  // namespace

static SocketLineGetter* INSTANCE = NULL;

SocketLineGetter::SocketLineGetter(const SocketDescription& desc)
    : buffer_(desc.bufferSize),
      desc_(desc),
      connected_(false),
      eof_(false),
      quitRequested_(false),
      lineQueue_(new LineQueue) {
  INSTANCE = this;
}

SocketLineGetter::~SocketLineGetter() {
  INSTANCE = NULL;
}

SocketLineGetter* SocketLineGetter::instance() {
  return INSTANCE;
}

string SocketLineGetter::getLine() {
  while (lineQueue_->empty())
    lineQueue_->push(readSocket());
  return lineQueue_->pop();
}

void SocketLineGetter::check(bool condition, const String& msg) {
  if (!condition) {
    eof_ = true;
    throw Exception(msg);
  }
}

static const char YAML_SEPARATOR[] = "\n---\n";

void SocketLineGetter::writeSocket(const char* data, int size) {
  string s(data, size);
  s += YAML_SEPARATOR;

  log("SocketLineGetter::tryToConnect write");
  tryToConnect();
  if (socket_.write(s.data(), s.size()) < 0)
    log("ERROR attempting to communicate with the master.");
}

void SocketLineGetter::tryToConnect() {
  if (connected_)
    return;

  log("SocketLineGetter::tryToConnect " + desc_.server +
      ":" + String(desc_.port));
  check(desc_.port, "No port assigned.");
  for (int attempts = 0; !connected_; ++attempts) {
    check(not desc_.tries or attempts <= desc_.tries, "Failed to connect");
    connected_ = socket_.connect(desc_.server, desc_.port, desc_.retryTimeout);
  }
  log(String("SocketLineGetter connected: ") + (connected_ ? "true" : "false"));
}

string SocketLineGetter::readSocket() {
  tryToConnect();
  while (true) {
    if (not socket_.isConnected())
      return "";

    {
      ScopedLock l(lock_);
      if (quitRequested_)
        return "";
    }
    int isReady = socket_.waitUntilReady(true, desc_.timeout);
    if (not isReady)
      continue;

    check(isReady >= 0, "StreamingSocket wait error");
    check(socket_.isConnected(), "Socket was ready, then disconnected.");

    int read = socket_.read(&buffer_.front(), buffer_.size(), false);

    check(read, "Socket was ready, but got zero data.");
    check(read > 0, "StreamingSocket read error");
    string s(&buffer_.front(), read);
    if (logAllSocketData)
      log2(s);
    return s;
  }
}

}  // namespace echomesh
