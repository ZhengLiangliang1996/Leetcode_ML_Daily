#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # non null can have 2 ##
        # null can have no #, so # at most 
        #    R 
        #   #  R
        #  /  #  # 
        nodes = preorder.split(',')
        count = 1
        for n in nodes:
            if count <= 0: return False 
            if n == '#':
                count -= 1
            else:
                count += 1
        return count == 0
