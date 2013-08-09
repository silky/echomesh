from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.command.show import Util
from echomesh.expression import Units

def units(_):
  Util.LOGGER.info('%s\n', Units.list_units())
