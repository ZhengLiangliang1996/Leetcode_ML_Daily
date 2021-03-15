#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

class Codec:
    def __init__(self):
        self.decode_map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        """
        shortUrl = "http://tinyurl.com/" + str(hash(longUrl))
        self.decode_map[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]
def main():
    pass


if __name__ == "__main__":
    main()

