# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:39:38 2024

@author: oyalu
"""
from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:


nums = [1,1,1,2,2,2,3]
k = 1
count = {}
freq = [[] for i in range(len(nums) + 1)]
# print(freq)
for n in nums:
    count[n] = 1 + count.get(n,0)
# print(count)

for n, c in count.items():
    freq[c].append(n)
# print(freq)

res = []
for i in range(len(freq) -1, 0, -1):
    # print(i)
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)