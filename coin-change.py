class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            ret = [float('inf') for _ in range(amount + 1)]
            ret[0] = 0
            for i in (range(amount + 1)):
                print(i)
                if i <= 0:
                    continue
                for c in coins:
                    if i == c:
                        ret[i] = 1
                    elif (i - c) >= 0:
                        ret[i] = min(ret[i], ret[i - c] + 1)
            if ret[amount] == float('inf'):
                return -1
            return ret[amount]
            