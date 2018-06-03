# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:36:26 2018

@author: bijiang
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

test = Solution()
s = "thisisatesttest"
#s = 'adau'
d = test.lengthOfLongestSubstring(s)
print(d)