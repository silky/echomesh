from __future__ import absolute_import, division, print_function, unicode_literals

import threading
import time

from echomesh.element import Element
from echomesh.expression.Units import INFINITY
from echomesh.util import Log

LOGGER = Log.logger(__name__)

# TODO: these should be config values.
DEFAULT_TIMEOUT = 1.0
DEFAULT_INTERVAL = INFINITY

class Loop(Element.Element):
  def __init__(self, parent, description, interval=1, name='Element.Loop',
               report_error_on_close=False, timeout=DEFAULT_TIMEOUT,
               full_slave=True, pause_on_exception=True, max_error_count=2):
    super(Loop, self).__init__(parent, description, full_slave=full_slave)
    self.name = name or repr(self)
    self.report_error_on_close = report_error_on_close
    self.interval = interval
    self.timeout = timeout
    self.pause_on_exception = pause_on_exception
    self.max_error_count = max_error_count
    self.error_count = 0

  def next_time(self, t):
    # TODO: is this right?
    return t

  def loop_target(self, t):
    pass

  def target(self):
    while self.is_running:
      try:
        self.single_loop()
      except:
        self.error_count += 1
        if self.is_running:
          if self.error_count < self.max_error_count:
            LOGGER.error('Thread %s reports an error:', self.name)
          if self.pause_on_exception and self.is_running:
            try:
              self.pause()
            except:
              pass
        elif self.report_error_on_close:
          LOGGER.error('Thread %s reports an error on close:', self.name)


  def _on_run(self):
    super(Loop, self)._on_run()
    self.next_loop_time = self.next_time(time.time())
    self.thread = threading.Thread(target=self.target)
    self.thread.daemon = True
    self.thread.start()

  def single_loop(self):
    now = time.time()
    if now >= self.next_loop_time:
      self.loop_target(now)
      self.next_loop_time = self.next_time(self.next_loop_time)
      if self.next_loop_time <= now:
        self.next_loop_time = self.next_time(now)

    if self.is_running:
      sleep_time = min(self.timeout, self.next_loop_time - now)
      if sleep_time > 0:
        time.sleep(sleep_time)
      else:
        LOGGER.error('Sleeping for negative time %s', sleep_time, limit=10)
