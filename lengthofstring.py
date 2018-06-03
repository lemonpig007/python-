# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:59:39 2018

@author: bijiang
"""

import numpy as np
class Solution:    
    def lengthOfLongestSubstring(self, s):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        sub_str = []
        sub_len = 0


        sub_str.append(s[0])
        for i in np.arange(1,len(s),1):
            repeat_flag = 0;
            for j in range(len(sub_str)):                
                if s[i] == sub_str[j]:
                    repeat_flag = 1
                    break
            if repeat_flag == 1:
                #if need output the substring 
                #str_norepeat = "".join(list3)  
                sub_len_new = len(sub_str)
                if sub_len_new > sub_len:
                    sub_len = sub_len_new
                while j>=0:  
                    sub_str.remove(sub_str[j])
                    j = j-1
            sub_str.append(s[i])
            
        sub_len_new = len(sub_str)
        if sub_len_new > sub_len:
            sub_len = sub_len_new
                 
        return(sub_len)
        

test = Solution()
#s = "thisisatesttest"
s = 'adau'
d = test.lengthOfLongestSubstring(s)
print(d)
                
