#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    
        # extract 2 numbers from number string 
        def extract(strnum):
            strnum = strnum.replace('i', '')
            imaginNeg = False 
            realNeg = False 
            if '+-' in strnum:
                strnum = strnum.replace('+-', '-')
                imaginNeg = True
            if strnum[0] == '-':
                strnum = strnum[1:]
                realNeg = True 
            if imaginNeg:
                print(strnum)
                real, imagin = list(map(int, strnum.split('-')))
            else:
                real, imagin = list(map(int, strnum.split('+')))
            if realNeg:
                real = -real
            if imaginNeg:
                imagin = -imagin
                
            return real, imagin
        
        real1, imagin1 = extract(num1)
        real2, imagin2 = extract(num2)
        
        real = real1 * real2 + (imagin1 * imagin2) * (-1)
        imagin1 = real1 * imagin2 + real2 * imagin1
        
        return str(real)+'+'+str(imagin1)+'i'
