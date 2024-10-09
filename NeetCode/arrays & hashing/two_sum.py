# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:37:48 2024

@author: oyalu
"""
from typing import List

# method 1
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     l = range(len(nums))
#     for i in l:
#         for j in l[i+1:]:
#             if nums[i] + nums[j] == target:
#                 return([i,j])
#                 break

# method 2
def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i,j in enumerate(nums):
        diff = target - j
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[j] = i

nums = [3,3]
target = 6

print(twoSum(nums, target))