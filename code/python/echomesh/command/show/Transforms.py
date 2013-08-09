from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.command.show import Util
from echomesh.expression import Transform

def transforms(_):
  for k in sorted(Transform.REGISTRY.keys()):
    Util.LOGGER.info('  %s\n%s\n', k,
                     Util.indent(Transform.REGISTRY.get_help(k), '    '))

HELP = """
Transforms are used to reshape curves.  Mathematically, they are invertible
mappings from [0, 1] onto [0, 1].

Whenever a transform is called for, you can name a single transform like

  sine

or you can compile a list of them, like

  sine.power.inverse.

"""
