# Algorithm: Brute Force O(n^2) solution, O(1) space
class Solution:
    def twoSum_old(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if  sum == target:
                    return [i, j]
        
        return []
    

    # Solution in O(n) Time complexity, O(n) space complexity    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map :
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]
        return []