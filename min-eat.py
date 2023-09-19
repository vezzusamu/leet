import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k:int) -> bool:
            remove = h * k
            if k == 0:
                return False
            for el in piles:
                remove_app = math.ceil(el / k)
                remove = remove - (remove_app) * k
                if remove < 0:
                    return False
            return True
                
        left = 0
        piles = sorted(piles)
        right = piles[-1]
        has_worked = -1
        while left <= right:
            mid = (left + right) // 2
            if eat(mid):
                right = mid - 1
                has_worked = mid
            else:
                left = mid + 1 
        return has_worked