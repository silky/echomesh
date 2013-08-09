from __future__ import absolute_import, division, print_function, unicode_literals

import six

from echomesh.command.show import Util

NO_NODES_ERROR = """\
There are no echomesh nodes in your network.

Since there should always be at least the computer running echomesh, this
indicates a serious problem with your networking or your configuration.

Consult the trouble-shooting guide for more information.
"""

def nodes(echomesh_instance):
  peers = echomesh_instance.peers.get_peers()
  if peers:
    for name, peer in six.iteritems(peers):
      Util.LOGGER.info('  %s: ', name)
      Util.info(peer, '    ')
  else:
    Util.LOGGER.error(NO_NODES_ERROR)
