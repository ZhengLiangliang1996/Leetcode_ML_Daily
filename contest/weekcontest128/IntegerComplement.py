#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        return int("".join(['0' if x == '1' else '1' for x in str(bin(n)[2:])]), 2)
