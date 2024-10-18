# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]


nums = [3,3,2,2,2,1]
k = 2
# nums = reversed(nums)
h = {}

for i in nums:
    h[nums.count(i)] = i

keys = sorted(h.keys(),reverse= True)
print([h[a] for a in keys])