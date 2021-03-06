#include <stdio.h>

#include <fstream>
#include <istream>
#include <iostream>
#include <string>

#include "echomesh/network/LineGetter.h"
#include "echomesh/network/ReadThread.h"
#include "echomesh/util/Quit.h"

#include "rec/util/thread/Callback.h"
#include "rec/util/STL.h"

namespace echomesh {

using namespace std;

ReadThread::ReadThread()
    : Thread("ReadThread"),
      lineGetter_(makeLineGetter("")) {
}

ReadThread::~ReadThread() {
  lineGetter_->requestQuit();
  stopThread(1000);
  rec::stl::deleteMapPointers(&messageMap_);
}

void ReadThread::run() {
  string s, str;
  log("starting read thread");
  while (not (threadShouldExit() or lineGetter_->eof())) {
    try {
      s = lineGetter_->getLine();

      if (threadShouldExit())
        break;

      if (s.find("---")) {  // If we don't find a separator.
        accum_.add(String(s.data(), s.size()));
        continue;
      }

      String yaml = accum_.joinIntoString("").trim();
      if (not yaml.length())
        continue;
      parse(yaml.toStdString());
      accum_.clear();
    } catch (YAML::Exception& e) {
      log(string("Yaml parsing error: ") + e.what() + (" in:\n" + str));
    } catch (Exception e) {
      log("ERROR: " + e.what_str());
      break;
    }
  }
  log("quitting");
  ::echomesh::quit();
}

void ReadThread::parse(const string& str) {
  ScopedLock l(lock_);
  if (lineGetter_->debug())
    log(str, false);

  istringstream s(str);
  YAML::Parser parser(s);
  parser.GetNextDocument(node_);
  node_["type"] >> type_;
  MessageMap::iterator i = messageMap_.find(type_);
  if (i == messageMap_.end())
    log("Didn't find message type " + type_);
  else
    (*i->second)();
}

}  // namespace echomesh
