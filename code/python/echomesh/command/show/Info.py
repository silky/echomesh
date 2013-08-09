from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.base import Name
from echomesh.command.show import Util

def info(_):
  Util.info(Name.info())

HELP = """
"show info" shows your machine's info record.

Info is the list of identifying information sent from your machine to other
echomesh nodes - it is how you see remote nodes identified when you "show nodes"
and it's how your machine will be identified remotely.

info is made up of the "names" and "addresses" of this machine.

See "help show names" and "help show addresses" for more information.

"""
