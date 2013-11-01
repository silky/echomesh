from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    #Echomesh
    Extension('echomesh', ['echomesh/*.py'],),
    Extension('echomesh.*', ['echomesh/*.py'],),
    Extension('echomesh.base', ['echomesh/base/*.py'],),
    Extension('echomesh.base.*', ['echomesh/base/*.py'],),
    Extension('echomesh.color', ['echomesh/color/*.py'],),
    Extension('echomesh.color.*', ['echomesh/color/*.py'],),
    Extension('echomesh.command', ['echomesh/command/*.py'],),
    Extension('echomesh.command.*', ['echomesh/command/*.py'],),
    Extension('echomesh.element', ['echomesh/element/*.py'],),
    Extension('echomesh.element.*', ['echomesh/element/*.py']),
    Extension('echomesh.event', ['echomesh/event/*.py'],),
    Extension('echomesh.event.*', ['echomesh/event/*.py'],),
    Extension('echomesh.expression', ['echomesh/expression/*.py']),
    Extension('echomesh.expression.*', ['echomesh/expression/*.py']),
    Extension('echomesh.expression.parse', ['echomesh/expression/parse/*.py']),
    Extension('echomesh.expression.parse.*', ['echomesh/expression/parse/*.py']),
    Extension('echomesh.graphics', ['echomesh/graphics/*.py']),
    Extension('echomesh.graphics.*', ['echomesh/graphics/*.py']),
    Extension('echomesh.light', ['echomesh/light/*.py']),
    Extension('echomesh.light.*', ['echomesh/light/*.py']),
    Extension('echomesh.network', ['echomesh/network/*.py']),
    Extension('echomesh.network.*', ['echomesh/network/*.py']),
    Extension('echomesh.pattern', ['echomesh/pattern/*.py']),
    Extension('echomesh.pattern.*', ['echomesh/pattern/*.py']),
    Extension('echomesh.remote', ['echomesh/remote/*.py']),
    Extension('echomesh.remote.*', ['echomesh/remote/*.py']),
    Extension('echomesh.sound', ['echomesh/sound/*.py']),
    Extension('echomesh.sound.*', ['echomesh/sound/*.py']),
    Extension('echomesh.util', ['echomesh/util/*.py']),
    Extension('echomesh.util.*', ['echomesh/util/*.py']),

    #External Dependencies
    Extension('external', ['external/*.py']),
    Extension('external.*', ['external/*.py']),
    Extension('*', ['external/*.py']),

    Extension('compatibility', ['external/compatibility/*.py']),
    Extension('compatibility.*', ['external/compatibility/*.py']),

    Extension('gittwit.*', ['external/gittwit/*.py']),
    Extension('gittwit.config', ['external/gittwit/config/*.py']),
    Extension('gittwit.git', ['external/gittwit/git/*.py']),
    Extension('gittwit.twitter', ['external/gittwit/twitter/*.py']),
    Extension('gittwit.util', ['external/gittwit/util/*.py']),
    Extension('gittwit.config.*', ['external/gittwit/config/*.py']),
    Extension('gittwit.git.*', ['external/gittwit/git/*.py']),
    Extension('gittwit.twitter.*', ['external/gittwit/twitter/*.py']),
    Extension('gittwit.util.*', ['external/gittwit/util/*.py']),

    Extension('httplib2', ['external/httplib2/*.py']),
    Extension('httplib2.*', ['external/httplib2/*.py']),

    Extension('oauth2', ['external/oauth2/*.py']),
    Extension('oauth2.clients', ['external/oauth2/clients/*.py']),
    Extension('oauth2.*', ['external/oauth2/*.py']),
    Extension('oauth2.clients.*', ['external/oauth2/clients/*.py']),

    Extension('parsedatetime', ['external/parsedatetime/*.py']),
    Extension('parsedatetime.*', ['external/parsedatetime/*.py']),

    Extension('pi3d', ['external/pi3d/*.py']),
    Extension('pi3d.constants', ['external/pi3d/constants/*.py']),
    Extension('pi3d.event', ['external/pi3d/event/*.py']),
    Extension('pi3d.loader', ['external/pi3d/loader/*.py']),
    Extension('pi3d.shape', ['external/pi3d/shape/*.py']),
    Extension('pi3d.sprite', ['external/pi3d/sprite/*.py']),
    Extension('pi3d.util', ['external/pi3d/util/*.py']),
    Extension('pi3d.*', ['external/pi3d/*.py']),
    Extension('pi3d.constants.*', ['external/pi3d/constants/*.py']),
    Extension('pi3d.event.*', ['external/pi3d/event/*.py']),
    Extension('pi3d.loader.*', ['external/pi3d/loader/*.py']),
    Extension('pi3d.shape.*', ['external/pi3d/shape/*.py']),
    Extension('pi3d.sprite.*', ['external/pi3d/sprite/*.py']),
    Extension('pi3d.util.*', ['external/pi3d/util/*.py']),

    Extension('pyparsing', ['external/pyparsing/*.py']),
    Extension('pyparsing.*', ['external/pyparsing/*.py']),

    Extension('requests', ['external/requests/*.py']),
    Extension('requests.packages', ['external/requests/packages/*.py']),
    Extension('requests.packages.charade', ['external/requests/packages/charade/*.py']),
    Extension('requests.packages.urllib3', ['external/requests/packages/urllib3/*.py']),
    Extension('requests.packages.urllib3.contrib', ['external/requests/packages/urllib3/contrib/*.py']),
    Extension('requests.packages.urllib3.packages', ['external/requests/packages/urllib3/packages/*.py']),
    Extension('requests.packages/urllib3.packages.ssl_match_hostname',
              ['external/requests/packages/urllib3/packages/ssl_math_hostname/*.py']),
    Extension('requests.*', ['external/requests/*.py']),
    Extension('requests.packages.*', ['external/requests/packages/*.py']),
    Extension('requests.packages.charade.*', ['external/requests/packages/charade/*.py']),
    Extension('requests.packages.urllib3.*', ['external/requests/packages/urllib3/*.py']),
    Extension('requests.packages.urllib3.contrib.*', ['external/requests/packages/urllib3/contrib/*.py']),
    Extension('requests.packages.urllib3.packages.*', ['external/requests/packages/urllib3/packages/*.py']),
    Extension('requests.packages/urllib3.packages.ssl_match_hostname.*',
              ['external/requests/packages/urllib3/packages/ssl_math_hostname/*.py']),

    Extension('simplejson', ['external/simplejson/*.py']),
    Extension('simplejson.*', ['external/simplejson/*.py']),
    Extension('yaml', ['external/yaml/*.py']),
    Extension('yaml.*', ['external/yaml/*.py'])
]

setup(
    name = 'Echomesh',
    ext_modules = cythonize(extensions)
)