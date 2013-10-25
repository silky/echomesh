from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "Echomesh",
    ext_modules = cythonize(["echomesh/*/*/*.py", "echomesh/*/*.py", "echomesh/*.py"])
)