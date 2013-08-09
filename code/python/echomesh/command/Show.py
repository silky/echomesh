from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.command.show import REGISTRY
from echomesh.command.show import Util

def _show_usage():
  return ('You can show any of the following values: \n  %s.\n' %
          REGISTRY.join_keys())

def show(echomesh_instance, *parts):
  if not parts:
    Util.LOGGER.info('\n' + _show_usage())
  else:
    for name in parts:
      try:
        function = REGISTRY.function(name)
      except:
        function = None
      if function:
        function(echomesh_instance)
      else:
        raise Exception("Didn't understand command 'show %s'. \n\n%s" %
                        (name, _show_usage()))

def _show_help():
  return _HELP + _show_usage()

HELP = _show_help

_HELP = """
"show" displays information about the current echomesh instance.
"""

