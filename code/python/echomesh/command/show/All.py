from __future__ import absolute_import, division, print_function, unicode_literals

import six

from echomesh.command.show import REGISTRY
from echomesh.command.show import Util

def _all(echomesh_instance):
  Util.LOGGER.info('')
  for name in sorted(REGISTRY.keys()):
    if name != 'all':
      Util.LOGGER.info('%s:', name)
      REGISTRY.function(name)(echomesh_instance)

def _all_help():
  return _HELP % (REGISTRY.join_keys())

FUNCTION = all
HELP = _all_help

_HELP =  """
Shows all information on all values:
  %s
"""

