class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_v = nums[0]
        max_v = nums[0]
        max_r = nums[0]
        for n in nums[1:]:
            tmp = n * max_v
            max_v = max(max_v * n, min_v * n, n)
            min_v = min(min_v * n, tmp, n)
            max_r = max(max_r, max_v)
        return max_r