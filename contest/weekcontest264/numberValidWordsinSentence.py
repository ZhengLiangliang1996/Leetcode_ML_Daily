#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        res = 0
        pattern = re.compile(r"^([a-z]+(-?[a-z]+)?)?[!|\.|,]?$")
        sentence_list = sentence.split(' ')
        for word in sentence_list:
            if word:
                result = pattern.findall(word)
                if result:
                    res += 1
        return res
