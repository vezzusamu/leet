import collections
from collections import deque
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                return n
            else:
                nums[n - 1] *= -1