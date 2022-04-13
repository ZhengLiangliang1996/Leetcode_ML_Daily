#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        res = []
        t = title.split(" ")
        print(t)
        for i in t:
            if len(i) == 1 or len(i) == 2:
                i = i.lower()
            else:
                i = i.lower()
                f = i[0].upper()
                i = f + i[1:]
            res.append(i)

        return ' '.join(res)
