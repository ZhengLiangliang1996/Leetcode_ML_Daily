#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [x for (x, _) in Counter(sorted(words)).most_common(k)]

