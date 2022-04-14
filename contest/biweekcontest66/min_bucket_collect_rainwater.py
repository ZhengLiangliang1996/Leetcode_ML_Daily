#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        if 'HHH' in street or street[:2]=='HH' or street[-2:]=='HH' or street=='H': return -1
        return street.count('H') - street.count('H.H')
        
        
