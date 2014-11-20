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

from __future__ import division

import hashlib


class CrazyHash(object):
    def __init__(self, composition, hasher=hashlib.sha1, sep='-'):
        self.composition = composition
        self.hasher = hasher()
        self.sep = sep

    @staticmethod
    def split_list(alist, wanted_parts=1):
        """
        http://stackoverflow.com/questions/752308/split-list-into-smaller-lists

        """
        length = len(alist)
        return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
                 for i in range(wanted_parts)]

    @property
    def digest_size(self):
        """The size of the resulting hash in bytes."""
        return len(self.digest().encode('utf-8'))

    @property
    def block_size(self):
        """The internal block size of the hash algorithm in bytes."""
        return self.hasher.block_size

    def update(self, arg):
        """
        Update the hash object with the string arg. Repeated calls are
        equivalent to a single call with the concatenation of all the
        arguments: `m.update(a); m.update(b)` is equivalent to
        `m.update(a+b)`.

        """
        return self.hasher.update(arg)

    def digest(self):
        """
        Return the digest of the strings passed to the `update()` method
        so far. This is a string of digest_size bytes which may contain
        non-ASCII characters, including null bytes.

        """
        values_hash = self.hasher.hexdigest()

        def get_components():
            chunks = self.split_list(values_hash, len(self.composition))
            for idx, subhash in enumerate(chunks):
                int_hash = int(subhash, 16)
                words = self.composition[idx]
                num_words = len(words)
                yield words[int_hash % num_words]

        return self.sep.join(get_components())

    def copy(self):
        """
        Return a copy (“clone”) of the hash object. This can be used to
        efficiently compute the digests of strings that share a common
        initial substring.

        """
        c = self.__class__(self.composition, lambda:None, self.sep)
        c.hasher = self.hasher.copy()
        return c
