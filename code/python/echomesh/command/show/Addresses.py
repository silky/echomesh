from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.base import Name
from echomesh.command.show import Util

def addresses(_):
  Util.info(Name.addresses())

HELP = """
Shows:
  This machine's current IP address.
  This machine's permanent MAC address.
"""
