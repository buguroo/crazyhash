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

from __future__ import absolute_import

try:
    BS = basestring
except NameError:
    BS = str

__all__ = []
COMPONENTS = {}


def _hasher(composition, *args, **kwargs):
    from .crazyhash import CrazyHash
    return CrazyHash(composition, *args, **kwargs)


def _create_hashers():
    from functools import partial
    from itertools import combinations
    from collections import Iterable

    import inspect

    from . import constants

    global COMPONENTS
    global __all__

    if not COMPONENTS:
        for name, value in inspect.getmembers(constants):
            if name.isupper() and \
                    isinstance(value, Iterable) and \
                    all(isinstance(x, BS) for x in value):
                COMPONENTS[name] = value

    if not __all__:
        for l in range(1, len(COMPONENTS) + 1):
            for composition in combinations(COMPONENTS.keys(), l):
                name = '_'.join(c.lower() for c in composition)
                func = partial(_hasher, [COMPONENTS[c] for c in composition])
                globals()[name] = func
                __all__.append(name)

_create_hashers()
