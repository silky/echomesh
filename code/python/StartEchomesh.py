#!/usr/bin/env python2.7

if __name__ == '__main__':
    import os
    import sys
    import platform

    cwd = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    build_folder = platform.uname()[0].lower() + '-' + platform.machine() + '-' + sys.version[:3]
    cython_plugin_folder = cwd + '/build/lib.%s' % build_folder

    sys.path.insert(0, cython_plugin_folder)

    from echomesh.base import Version

    if Version.TOO_OLD:
        from echomesh.util import TooOld
        TooOld.too_old()
        exit(-1)

    from echomesh import Main
    Main.main()
