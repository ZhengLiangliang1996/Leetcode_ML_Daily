#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed utfnder terms of the MIT license.

from functools import wraps
def logit(logfile='out.log'):
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(logfile)
            print(func.__name__ + 'was called')
            return func(*args, **kwargs)
        return wrapper
    return logger 

@logit(logfile='func2.log')
def example(x):
    return x*x

print(example(4))

# decorator class 
class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(self.logfile)
            print(func.__name__ + 'was called')
            return func(*args, **kwargs)
        return wrapper

@logit()
def myfunc1():
    pass

myfunc1()
