#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def solveSudoku(self, brd):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        box = [[0 for _ in range(9)] for _ in range(9)]
        rows= [[0 for _ in range(9)] for _ in range(9)]
        cols= [[0 for _ in range(9)] for _ in range(9)]
        
        # mark the existed brd 
        for i in range(len(brd)):
            for j in range(len(brd[0])):
                if brd[i][j] != '.':
                    v = int(brd[i][j]) - 1
                    box_x = i // 3
                    box_y = j // 3
                    rows[i][v] = 1
                    cols[j][v] = 1
                    box[box_x*3 + box_y][v] = 1
                    
        def get_idx(idx):
            x = idx // 9
            y = idx % 9
            return x, y
        
        def dfs(idx):
            if idx == 81: return True 
            x, y = get_idx(idx)
            
            # go to the next grid
            if brd[x][y] != '.': return dfs(idx+1)
            
            # choice 
            box_x = x // 3
            box_y = y // 3
            for v in range(1, 10):
                if not box[box_x*3 + box_y][v-1] and not rows[x][v-1] and not cols[y][v-1]:
                    
                    box[box_x*3 + box_y][v-1] =  1
                    rows[x][v-1] = 1
                    cols[y][v-1] = 1
                    brd[x][y] = str(v)
                    
                    if dfs(idx+1):
                        return True 
                    
                    box[box_x*3 + box_y][v-1] =  0
                    rows[x][v-1] = 0
                    cols[y][v-1] = 0
                    brd[x][y] = '.'
        
        dfs(0)
        
                
            
        
