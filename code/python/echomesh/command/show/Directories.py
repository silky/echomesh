from __future__ import absolute_import, division, print_function, unicode_literals

from echomesh.base import Path
from echomesh.command.show import Util

def directories(_):
  Util.info(Path.info())

HELP = """
"show path" shows directories that contain files used by echomesh:

  * The asset directory, where images, audio and other assets are stored.
  * The code directory, where the echomesh Python code is stored.
  * The command directory, which holds configuration files and scores.
  * The project directory, the project root containing assets and commands.
  * The echomesh directory, which is the root of the echomesh installation.
"""
