class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_n = -999999999
        curr_n = max_n
        for n in nums:
            if curr_n < 0:
                curr_n = n
            else:
                curr_n += n
            if curr_n > max_n:
                max_n = curr_n
        return max_n