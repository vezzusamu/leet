class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(len(nums)):
            if i < 2:
                continue
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]