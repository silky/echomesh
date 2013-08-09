from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.command.show import Util

def broadcast(echomesh_instance):
  message = 'ON' if echomesh_instance.broadcasting() else 'off'
  Util.LOGGER.info('  Broadcast is %s\n', message)

HELP = """
Shows if this echomesh node is in broadcast made, meaning that its run and pause
commands are sent to all other nodes.

When a node is in broadcast mode, the standard "echomesh:" prompt is replaced
by "echomesh!"

"""
