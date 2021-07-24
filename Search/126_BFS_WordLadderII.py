#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordlist=set(wordList)
        res= []
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword=w[:i] + c + w[i+1:]
                            if newword in wordlist:
                                newlayer[newword] += [j+[newword] for j in layer[w]]
            wordlist -=set(newlayer.keys())
            layer = newlayer
        
        return res

