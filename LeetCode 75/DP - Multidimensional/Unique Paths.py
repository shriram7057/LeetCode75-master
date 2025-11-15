class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1] * n  # first row = all 1's

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]
