from typing import List

'''  method 1'''
def containsDuplicate(nums: List[int]) -> bool:
    l = set()   
    for i in nums:
        if i not in l:
            l.add(i)
        else:
            return True
            break
    else:
        return False
    
case1 = [1,2,3,1]
case2 = [1,2,3,4]
case3 = [1,1,1,3,3,4,3,2,4,2]

r1,r2,r3 = containsDuplicate(case1), containsDuplicate(case2), containsDuplicate(case3)
print('r1', r1,'r2',r2, 'r3',r3)


''' method 2 '''

# class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums = sorted(nums)

    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i-1]:
    #             return True
    #     else:
    #         return False
# r1,r2,r3 = containsDuplicate(case1), containsDuplicate(case2), containsDuplicate(case3)
# print('r1', r1,'r2',r2, 'r3',r3)

''' method 3 '''
# def containsDuplicate(self, nums: List[int]) -> bool:
#     hashset = set()
#     for i in nums:
#         if i in hashset:
#             return True
#         hashset.add(i)
#     return False

# r1,r2,r3 = containsDuplicate(case1), containsDuplicate(case2), containsDuplicate(case3)
# print('r1', r1,'r2',r2, 'r3',r3)