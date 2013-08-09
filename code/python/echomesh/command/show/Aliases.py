from __future__ import absolute_import, division, print_function, unicode_literals

import six

from echomesh.command import Aliases
from echomesh.command.show import Util

def aliases(*_):
  aliases = Aliases.instance()
  if aliases:
    Util.info(aliases)
  else:
    Util.LOGGER.info('  No aliases\n')

HELP = """
Shows all the command aliases that have been registered.
"""
