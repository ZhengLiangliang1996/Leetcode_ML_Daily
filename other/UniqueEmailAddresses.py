#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air.localdomain>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        def checkEmail(email):
            res = ''
            local, domain = email.split('@')
            if local[0] == '+':
                return res 
            local = local.replace('.', '')
            if '+' in local:
                idx = local.index('+')
                local = local[:idx]
            res = local + '@' + domain
            return res 
        res = []
        for e in emails:
            res.append(checkEmail(e))
    

        return len(list(set(res)))
