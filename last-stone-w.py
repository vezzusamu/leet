class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            res = first - second
            if res:
                heapq.heappush(stones, res)
        
        if stones:
            return abs(stones[0])
        return 0