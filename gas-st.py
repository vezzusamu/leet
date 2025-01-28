class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gas[i] -= cost[i]
        chosen = 0
        s = gas[0]
        for i in range(1, len(gas)):
            if s + gas[i] < gas[i]:
                s = gas[i]
                chosen = i
            else:
                s += gas[i]
        s = gas[chosen]
        i = chosen
        while True:
            i += 1
            if(i >= len(gas)):
                i = 0
            if(i == chosen):
                if (s >= 0):
                    return chosen 
                return -1
            s += gas[i]
            if(s < 0):
                return -1
        return chosen