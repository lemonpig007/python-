# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:30:17 2018

@author: bijiang
"""

import numpy as np
class Solution:
    def occupy(self,A,area,ghost):
#l is the x coordinate in aera and k is the y coordinate in area
        area_arr = np.array(area)
        l = area_arr[:,0]
        k = area_arr[:,1]
        area = []
        if(ghost):
            for x in range(len(l)):
                if A[l[x]+1,k[x]] != 0 and l[x]+1 < 10000 and l[x]+1>=0:                    
                    A[l[x]+1,k[x]] = 0
                    area.append([l[x]+1,k[x]])
                if A[l[x]-1,k[x]] != 0 and l[x]-1 < 10000 and l[x]-1>=0:
                    A[l[x]-1,k[x]] = 0
                    area.append([l[x]-1,k[x]])
                if A[l[x],k[x]+1] != 0 and k[x]+1 < 10000 and k[x]+1>=0:
                    A[l[x],k[x]+1] = 0
                    area.append([l[x],k[x]+1])
                if A[l[x],k[x]-1] != 0 and k[x]-1 < 10000 and k[x]-1>=0:
                    A[l[x],k[x]-1] = 0
                    area.append([l[x],k[x]-1])
        else:
            for x in range(len(l)):
                if A[l[x]+1,k[x]] == 0xff and l[x]+1 < 10000 and l[x]+1>=0: 
                    A[l[x]+1,k[x]] = 1
                    area.append([l[x]+1,k[x]])
                if A[l[x]-1,k[x]] == 0xff and l[x]-1 < 10000 and l[x]-1>=0:
                    A[l[x]-1,k[x]] = 1
                    area.append([l[x]-1,k[x]])
                if A[l[x],k[x]+1] == 0xff and k[x]+1 < 10000 and k[x]+1>=0:
                    A[l[x],k[x]+1] = 1
                    area.append([l[x],k[x]+1])
                if A[l[x],k[x]-1] == 0xff and k[x]-1 < 10000 and k[x]-1>=0:
                    A[l[x],k[x]-1] = 1
                    area.append([l[x],k[x]-1])
        return (area)
    
    
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
         """
#initialization       
        A = np.ones([10001,10001])*0xff
       # for i in range(10000):
       #     for j in range(10000):
       #         A[i,j] = 0xff
            
        area_ghost = []
        area_man = []
        area_man.append([0,0])
    
#add all the ghosts position to list
        for i in range(np.shape(ghosts)[0]):
            area_ghost.append(ghosts[i])
        
#fill the map
        while A[target[0],target[1]] == 0xff:
            area_ghost = self.occupy(A,area_ghost,True)
            area_man = self.occupy(A,area_man,False)
        
#check who occupy the target
        if A[target[0],target[1]] == 1:
            return (True)
        else:
            return (False) 
game = Solution();  
ghosts = [[1,0],[0,3]]
target =[0,1]  
makeit = game.escapeGhosts(ghosts, target)
print(makeit)