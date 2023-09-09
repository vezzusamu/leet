class Solution:
    #O(nlogn)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0:
            return 0
        max = 1
        current = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current = current + 1
            elif not nums[i] == nums[i-1]:
                current = 1
            if current > max:
                max = current
        return max
    
    #O(n) Based on set
    def longestConsecutive_extra(self, nums: List[int]) -> int:
        nums = set(nums)
        max = 0
        for num in nums:
            if num - 1 not in nums:
                current = 1
                while num + 1 in nums:
                    num = num + 1
                    current = current + 1
                if current > max:
                    max = current
        return max