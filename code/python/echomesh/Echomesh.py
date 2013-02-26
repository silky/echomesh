from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.element import ScoreMaster
from echomesh.graphics import Display
from echomesh.network import PeerSocket
from echomesh.network import Peers
from echomesh.sound import Microphone
from echomesh.util import Log
from echomesh.util.thread import Keyboard
from echomesh.util.thread.MasterRunnable import MasterRunnable

LOGGER = Log.logger(__name__)

class Echomesh(MasterRunnable):
  INSTANCE = None

  def __init__(self):
    super(Echomesh, self).__init__()
    if Echomesh.INSTANCE:
      LOGGER.error('There is more than one instance of Echomesh')
    else:
      Echomesh.INSTANCE = self

    self.score_master = ScoreMaster.ScoreMaster()
    self.peers = Peers.Peers(self)
    self.socket = PeerSocket.PeerSocket(self, self.peers)

    self.display = Display.Display()
    self.mic = Microphone.microphone(self._mic_event)
    self.keyboard = Keyboard.keyboard(self)

    self.add_mutual_stop_slave(self.socket, self.keyboard, self.mic)
    self.add_slave(self.score_master)
    self.add_slave(self.display)
    self.set_broadcasting(False)
    self.quitting = False

  def broadcasting(self):
    return self._broadcasting

  def set_broadcasting(self, b):
    self._broadcasting = b
    self.keyboard.alert_mode = b

  def send(self, **data):
    self.socket.send(data)

  def handle(self, event):
    return self.score_master.handle(event)

  def loop(self):
    self.display.loop()

  def join(self):
    self.keyboard.thread.join()

  def _mic_event(self, level):
    self.send(type='event', event_type='mic', key=level)

