from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.util import Log
from echomesh.util.thread.MasterRunnable import MasterRunnable
from gittwit.twitter.Search import Loop

class MultiSearch(MasterRunnable):
  def __init__(self, callback, interval=2, preload=1, name='MultiSearch'):
    super(MultiSearch, self).__init__()
    self.callback = callback
    self.interval = interval
    self.preload = preload
    self.name = name
    self.searches = {}
    self.index = 0

  def add(self, search):
    if search in self.searches:
      Log.LOGGER.error('Already searching %s')
    else:
      self.index += 1
      loop = Loop(search, self.callback, self.interval, self.preload,
                  name = '%s:%s' % (self.name, self.index))
      self.searches[search] = loop
      self.add_slave(loop)
      loop.run()

  def remove(self, search):
    loop = self.searches.get(search)
    if loop:
      del self.searches[search]
      loop.stop()
      self.remove_slave(loop)

    else:
      Log.LOGGER.error('No search %s', search)

