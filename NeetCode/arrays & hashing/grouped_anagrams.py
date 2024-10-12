# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 08:33:17 2024

@author: oyalu
"""
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


s = ["eat","tea","tan","ate","nat","bat"]

# sort = sorted([sorted(i) for i in s])
# print(sort)

# has = {}

# for i in s:
#     if sorted(i) not in [sorted(a) for a in has.keys()]:
#         has[tuple(sorted(i))] = [i]
#     elif sorted(i) in [sorted(a) for a in has.keys()]:
#         has[tuple(sorted(i))].append(i)
# print(has.values())


from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

res = defaultdict(list)
# for st in strs:
#     count = [0] * 26
#     # print(count)
#     for char in st:
#         count[ord(char) - ord("a")] += 1



for s in strs:
    res[tuple(sorted(s))].append(s)
print(res.values())