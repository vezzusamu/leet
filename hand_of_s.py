class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        m = {}
        for n in hand:
            m[n] = m.get(n, 0) + 1
        
        min_h = list(m.keys())
        heapq.heapify(min_h)

        while(min_h):
            f = min_h[0]
            for i in range(f, groupSize + f):
                if i not in m:
                    return False
                m[i] -= 1
                if m[i] <= 0:
                    el = heapq.heappop(min_h)
                    if not (el == i):
                        return False
        return True