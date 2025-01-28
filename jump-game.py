class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 1
        for n in nums:
            if curr <= 0:
                return False
            curr = max(curr-1, n)
        return True