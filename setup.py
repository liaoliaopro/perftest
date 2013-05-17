from distutils.core import setup
from  distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('func_cython', ['func_cython.pyx', 't.c'])]

setup(
    name = 'func_cython',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

