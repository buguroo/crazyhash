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

import hashlib
import imp
import sys

from . import constants as CONS
from .crazyhash import CrazyHash

class CrazyHashLoader:
    def load_module(self, fullname):

        try:
            return sys.modules[fullname]
        except KeyError:
            pass

        m = imp.new_module(fullname)
        m.__file__ = "crazyhash:" + fullname
        m.__path__ = []
        m.__loader__ = self

        # crazyhash.colors_nato => ['colors', 'nato']
        components = fullname.split('.')[-1].split('_')

        class Hasher(CrazyHash):
            try:
                composition = [getattr(CONS, n.upper()) for n in components]
            except AttributeError as exc:
                raise ImportError(exc)

        m.Hasher = Hasher

        sys.modules.setdefault(fullname, m)
        return m


class CrazyHashFinder:
    def find_module(self, fullname, path=None):
        if fullname.startswith("crazyhash."):
            return CrazyHashLoader()
        return None


__path__ = []
sys.meta_path.append(CrazyHashFinder())
