class Solution:
    def maxArea(self, height: List[int]) -> int: 
        current_max = 0
        h = len(height) - 1
        l = 0
        while l < h:
            lowest = min(height[l], height[h])
            current = lowest * (h - l)
            current_max = max(current, current_max)
            if height[l] < height[h]:
                l = l + 1
            else:
                h = h - 1
        return current_max