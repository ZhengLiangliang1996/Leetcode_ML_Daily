#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        # initialize variables
        max_length = 1
        freq = [0] * 26  # count the frequency of each character
        left = 0
        max_freq = 0

        # iterate through the string
        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, freq[ord(s[right]) - ord('A')])

            # check if we need to change characters
            if (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

