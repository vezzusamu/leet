class Solution:
    def _n_contiguous_for_level(self, n, heights: List[int]) -> int:
        max_cont = 0
        current_cont = 0
        for height in heights:
            if n <= height:
                current_cont +=1
                max_cont = max(current_cont, max_cont)
            else:
                current_cont = 0
        return max_cont

    def largestRectangleArea(self, heights: List[int]) -> int:
        level = max(heights)
        max_area = 0
        for i in range(level+1):
            current = self._n_contiguous_for_level(i, heights)
            area = i * current
            max_area = max(max_area, area)
        return max_area
