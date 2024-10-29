# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
from typing import List

nums = [5,5,5,5,6,3,3,3,2,2,2,1]
# nums = [1,2]
k = 2
# nums = reversed(nums)
h = {}

# for i in nums:
#     h[nums.count(i)] = i

# print('hash',h)
# freq = list(h.keys())
# print('freq', freq)

# required = sorted(freq, reverse=True)[:k]
# print(required)
# print([h[req] for req in required])
# sorted_keys = sorted(h.keys(),reverse= True)
# # print('descending keys', keys)
# print([h[a] for a in keys])

# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     h = {}

#     for i in nums:
#         h[nums.count(i)] = i

#     freq = sorted(h.keys(), reverse= True)[:k]
#     return [h[req] for req in freq]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

freq_table = {}
for num in nums:
    freq_table[num] = 1 + freq_table.get(num, 0)

print(freq_table)

bucket = [[] for i in range(len(nums) + 1)]
print(bucket)

for num, freq in freq_table.items():
    bucket[freq].append(num)
print(bucket)

result = []
for i in range(len(bucket)-1, 0, -1):
    for j in bucket[i]:
        result.append(j)
        if len(result) == k:
            print(result)
            break
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_table = {}
        for num in nums:
            freq_table[num] = 1 + freq_table.get(num, 0)
            
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in freq_table.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
                    break

print(Solution.topKFrequent(nums, k))
                