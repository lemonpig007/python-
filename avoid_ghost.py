c# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:40:22 2018

@author: bijiang
"""
import numpy as np


def occupy(A,area,ghost):
#l is the x coordinate in aera and k is the y coordinate in area
    area_arr = np.array(area)
    l = area_arr[:,0]
    k = area_arr[:,1]
    area = []
    if(ghost):
        for x in range(len(l)):
            if A[l[x]+1,k[x]] != 0 and l[x]+1 < 100 and l[x]+1>=0:                    
                A[l[x]+1,k[x]] = 0
                area.append([l[x]+1,k[x]])
            if A[l[x]-1,k[x]] != 0 and l[x]-1 < 100 and l[x]-1>=0:
                A[l[x]-1,k[x]] = 0
                area.append([l[x]-1,k[x]])
            if A[l[x],k[x]+1] != 0 and k[x]+1 < 100 and k[x]+1>=0:
                A[l[x],k[x]+1] = 0
                area.append([l[x],k[x]+1])
            if A[l[x],k[x]-1] != 0 and k[x]-1 < 100 and k[x]-1>=0:
                A[l[x],k[x]-1] = 0
                area.append([l[x],k[x]-1])
    else:
        for x in range(len(l)):
            if A[l[x]+1,k[x]] == 0xff and l[x]+1 < 100 and l[x]+1>=0: 
                A[l[x]+1,k[x]] = 1
                area.append([l[x]+1,k[x]])
            if A[l[x]-1,k[x]] == 0xff and l[x]-1 < 100 and l[x]-1>=0:
                A[l[x]-1,k[x]] = 1
                area.append([l[x]-1,k[x]])
            if A[l[x],k[x]+1] == 0xff and k[x]+1 < 100 and k[x]+1>=0:
                A[l[x],k[x]+1] = 1
                area.append([l[x],k[x]+1])
            if A[l[x],k[x]-1] == 0xff and k[x]-1 < 100 and k[x]-1>=0:
                A[l[x],k[x]-1] = 1
                area.append([l[x],k[x]-1])
    return area
                
              

def toTarget():
    A = np.zeros([101,101])
    ghost = [[0,77]]
    target = [50,50]
    for i in range(100):
        for j in range(100):
            A[i,j] = 0xff
            
    area_ghost = []
    area_man = []
    area_man.append([0,0])
#add all the ghosts position to list
    for i in range(np.shape(ghost)[0]):
        area_ghost.append(ghost[i])
#fill the map
    print(A[target[0],target[1]])
    while A[target[0],target[1]] == 0xff:
        area_ghost = occupy(A,area_ghost,True)
        area_man = occupy(A,area_man,False)
#check who occupy the target
    if A[target[0],target[1]] == 1:
        return True
    else:
        return False
        
makeit = toTarget()   
print(makeit)
    
   
            
        
        
        
        
            