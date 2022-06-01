#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end = []
    
    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        self.end.append((p, len(word)+1))
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 前缀树
        trie=Trie()
        for word in set(words):
            trie.insert(word[::-1])
        res=0
        for el,length in trie.end:
            if not el:
                res+=length
        return res
