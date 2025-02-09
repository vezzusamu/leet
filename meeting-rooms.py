from heapq import heapify, heappush, heappop 


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        minHeap = []
        heapify(minHeap)
        for interval in intervals:
            if minHeap:
                m = heappop(minHeap)
                if m > interval.start:
                    heappush(minHeap, m)
            heappush(minHeap,interval.end)
        return len(minHeap)