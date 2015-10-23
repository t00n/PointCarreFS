#!/usr/bin/env python2

from distutils.core import setup

setup(name='pointcarrefs',
      version='0.1',
      description='Mount pointcarre.vub.ac.be with fuse',
      author='Tichrist',
      author_email='',
      url='',
      install_requires=['fusepy'],
      py_modules = ['pointcarre', 'config'],
      scripts = ['pointcarrefs']
     )