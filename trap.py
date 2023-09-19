class Solution:
    def trap(self, height: List[int]) -> int:
        current_tot = 0
        h = len(height) - 1
        l = 0
        h_m = 0
        l_m = 0
        while l < h:
            h_m = max(height[h], h_m)
            l_m = max(height[l], l_m)
            current = 0
            if height[h] > height[l]:
                l = l + 1
                current = l_m - height[l]
            else:
                h = h - 1
                current = h_m - height[h]
            if current < 0:
                continue 
            current_tot = current +  current_tot

        return current_tot