from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.command.show import Util

def variables(instance):
  results = []
  for name, v in six.iteritems(instance.score_master.elements):
    _variables([name], v, results)

  if results:
    for path, value in sorted(results):
      Util.LOGGER.info('  %s = %s', '.'.join(path), value)
    Util.LOGGER.info('')
  else:
    Util.LOGGER.info('  No variables have been set.\n')

HELP = """
Show all variables for each element currently running.
"""
