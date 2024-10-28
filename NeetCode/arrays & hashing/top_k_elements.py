# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
from typing import List

# nums = [3,3,2,2,2,1]
nums = [1,2]
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

def get_key_by_value(dictionary, target_value):
    return next(key for key, value in dictionary.items() if value == target_value)

# Example dictionary
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "lime": "green"
}

# Find the key for the value "yellow"
fruit_name = get_key_by_value(fruits, "yellow")
print(f"The fruit that is yellow is: {fruit_name}")

# Find the key for the value "green"
fruit_name = get_key_by_value(fruits, "green")
print(f"The fruit that is green is: {fruit_name}")