from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.base import Name
from echomesh.command.show import Util

def elements(echomesh_instance):
  inf = echomesh_instance.score_master.info()
  if inf:
    Util.info(inf)
  else:
    Util.LOGGER.info('  No elements have been loaded into memory.\n')

HELP = """
"show elements" shows all the elements that have been loaded, as well as the
time they were started.

See "help start" and "help pause" for more information.
"""
