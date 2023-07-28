from typing import List;

class Solution:
    #O(n^2) solution Time, exceeds time limit
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]: #nums[i+1:] creates a list of all elements after nums[i]
                return True
            
    #O(n) solution Time, O(n) space
    def containsDuplicateUsingSet(self, nums: List[int]) -> bool:
        distinct_nums = list(set(nums)) #set() removes duplicates
        return len(nums) != len(distinct_nums)
            
    #O(n log n) solution Time, O(1) space
    def containsDuplicateBySorting(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False