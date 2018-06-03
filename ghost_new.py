# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:37:49 2018

@author: bijiang
"""

import numpy as np
class Solution:    
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
         """
    
#add all the ghosts position to list
        distance = []
        for i in range(np.shape(ghosts)[0]):
           distance.append(abs(ghosts[i][0]-target[0]) + abs(ghosts[i][1]-target[1]))
        min_dis = min(distance)
        
        dis_man = abs(target[0])+abs(target[1])
        
#check who occupy the target
        if min_dis - dis_man > 0:
            return (True)
        else:
            return (False) 
game = Solution();  
ghosts = [[1,0],[0,3]]
target =[0,1]  
makeit = game.escapeGhosts(ghosts, target)
print(makeit)