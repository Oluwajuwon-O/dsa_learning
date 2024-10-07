# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:51:47 2024

@author: oyalu
"""
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


# from collections import Counter
# print(Counter('anagram'))



def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    for c in count_s:
        return count_s.get(c) == count_t.get(c,0)

s,t = 'anagram', 'nagaram'
print(isAnagram(s,t))
