from __future__ import absolute_import, division, print_function, unicode_literals

import contextlib
import os
import os.path
import sys
import threading
import time
import traceback

from echomesh.command import Processor
from echomesh.command import Router
from echomesh.command import Score

from echomesh.config import Config

from echomesh.graphics import Display

from echomesh.network import Address
from echomesh.network import DataSocket
from echomesh.network import Discovery
from echomesh.network import Peers

from echomesh.sound import Microphone
from echomesh.sound import SetOutput

from echomesh.util import Closer
from echomesh.util import File
from echomesh.util import Log

LOGGER = Log.logger(__name__)
ECHOMESH = None

class Echomesh(Closer.Closer):
  INSTANCE = None

  def __init__(self):
    super(Echomesh, self).__init__()
    if Echomesh.INSTANCE:
      LOGGER.error('There is more than one instance of Echomesh')
    else:
      Echomesh.INSTANCE = self

    self.peers = Peers.Peers(self)
    callbacks = Router.router(self, self.peers)
    timeout = Config.get('discovery', 'timeout')
    port = Config.get('discovery', 'port')
    self.data_socket = DataSocket.data_socket(port, timeout, callbacks)

    if self.data_socket:
      self.display = Display.display(self)
      self.microphone = Microphone.Microphone(self._mic_event)
      self.score = Score.make_score()

  def start(self):
    if not self.data_socket:
      return
    try:
      self.peers.start()
      self.microphone.start()
      self.data_socket.start()

      if Config.is_control_program():
        threading.Thread(target=self._keyboard_input).start()

      if self.display:
        self.display.loop()
      self._join()
    except:
      LOGGER.critical(traceback.format_exc())
    finally:
      self.close()
      LOGGER.info('Finished Echomesh')

  def remove_local(self):
    # TODO: this probably doesn't work any more.
    try:
      Config.remove_local()
      self.microphone.set_config()

    except OSError as e:
      LOGGER.warn("No local file %s" % Config.LOCAL_CHANGED_FILE)

    try:
      os.remove(LOCAL_SCORE)
    except OSError as e:
      LOGGER.warn("No local score file %s", LOCAL_SCORE)

  def send(self, **data):
    data['source'] = Address.NODENAME
    self.data_socket.send(data)

  def receive_event(self, event):
    self.score.receive_event(event)

  def set_score(self, score):
    File.yaml_dump_all(LOCAL_SCORE, score)
    self.score.set_score(score)

  def set_config(self, config):
    Config.change(config)
    self.microphone.set_config()

  def close(self):
    if self.is_open:
      Closer.on_exit()
      LOGGER.info('closing')
      self.data_socket.close()
      super(Echomesh, self).close()
      self.microphone.close()
      self.display and self.display.close()
      self.score.close()
      self._join()

  def _mic_event(self, level):
    self.send(type='event', event='mic', key=level)

  def _keyboard_input(self):
    sleep = Config.get('opening_sleep')
    if sleep:
      time.sleep(sleep)

    print()
    print('           echomesh')
    print()
    print('Type help for a list of commands')
    print()
    while self.is_open:
      if not Processor.process(raw_input('echomesh: ').strip(), self):
        self.close()

  def _join(self):
    LOGGER.debug('joining')
    self.display and self.display.join()
    LOGGER.debug('display joined')
    self.data_socket.join()
    LOGGER.debug('discovery joined')
    self.microphone.join()
    LOGGER.debug('mic joined')
    self.score.join()
    LOGGER.debug('joined')


if __name__ == '__main__':
  if Config.get('autostart') or len(sys.argv) < 2 or sys.argv[1] != 'autostart':
    SetOutput.set_output(Config.get('audio', 'output', 'route'))
    Echomesh().start()
  else:
    LOGGER.info("Not autostarting because autostart=False")
