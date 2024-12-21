class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in reversed(range(len(cost))):
            if(i + 1 >= len(cost)):
                cost_step_1 = 0
            else:
                cost_step_1 = cost[i + 1]
            if(i + 2 >= len(cost) ):
                cost_step_2 = 0
            else:
                cost_step_2 = cost[i + 2]
            cost[i] = min(cost[i]+cost_step_1, cost[i]+cost_step_2)
        return min(cost[i], cost[i+1])