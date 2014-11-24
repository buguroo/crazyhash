#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of crazyhash.
# 
# crazyhash is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# crazyhash is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with crazyhash.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGELOG = open(os.path.join(here, 'CHANGELOG.txt')).read()

version = '0.0.2'

setup(name='crazyhash',
      version=version,
      description="Natural language hashing library.",
      long_description=README + '\n\n' + CHANGELOG,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
          "Topic :: Security :: Cryptography"
      ],
      keywords='keyword hash',
      author='Roberto Abdelkader Martínez Pérez'.encode('utf-8'),
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/buguroo/crazyhash',
      license='LGPLv3',
      packages=find_packages(b'src'),
      package_dir={'': b'src'},
      include_package_data=True,
      zip_safe=False)
