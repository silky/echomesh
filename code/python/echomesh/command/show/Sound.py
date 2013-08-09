from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.command.show import Util
from echomesh.sound import Sound

def sound(_):
  Util.info(Sound.info())
