#!/usr/bin/env python2.7

if __name__ == '__main__':
    import os
    import sys

    cwd = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    cython_plugin_folder = cwd + '/build/lib.linux-x86_64-2.7'

    sys.path.insert(0, cython_plugin_folder)

    from echomesh.base import Version

    if Version.TOO_OLD:
        from echomesh.util import TooOld
        TooOld.too_old()
        exit(-1)

    from echomesh import Main
    Main.main()
