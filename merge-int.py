class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i1 = 0
        i2 = 1
        intervals = sorted(intervals)
        while(i2 < len(intervals)):
            if intervals[i1][1] >= intervals[i2][0]:
                intervals[i1][1] = max(intervals[i2][1], intervals[i1][1])
                del intervals[i2]
            else:
                i1 += 1
                i2 += 1
        return intervals