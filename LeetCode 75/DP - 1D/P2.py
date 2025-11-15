class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 1:
            return cost[0]

        dp1, dp2 = 0, 0   # dp1 = cost to reach step i-1, dp2 = cost to reach step i-2

        for i in range(2, n + 1):
            new_dp = min(dp1 + cost[i - 1], dp2 + cost[i - 2])
            dp2, dp1 = dp1, new_dp

        return dp1
