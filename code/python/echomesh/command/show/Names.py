from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.base import Name
from echomesh.command.show import Util

def names(_):
  Util.info(Name.names())

HELP = """
"show names" shows you the following information about this echomesh node:

  * The machine name (also called the uname for Linux machines).
  * The echomesh name.  This is by default the machine name but can be changed
    in the echomesh configuration.
  * The echomesh tags for this machine, which are also set in the configuration.
"""
