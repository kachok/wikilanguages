# -*- coding: utf-8 -*-
 
from distutils.core import setup
 
setup(name='wikilanguages',
      version='0.1',
      description='Python library to manipulate with all the languages used in Wikipedia projects.',
      author='James Dennis',
      author_email='dmitry.kachaev@gmail.com',
      url='http://github.com/kachok/wikilanguages',
      packages=['wikilanguages'],
      package_data={'wikilanguages': ['resources/*']})