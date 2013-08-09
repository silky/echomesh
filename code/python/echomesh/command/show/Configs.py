from __future__ import absolute_import, division, print_function, unicode_literals

import six

from echomesh.base import Config
from echomesh.base import Yaml
from echomesh.command.show import Util

def configs(_):
  Util.LOGGER.info('\n' + Yaml.encode_one(Config.MERGE_CONFIG.config))
