class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # dp[j] stores the minimum cost to reach step j
        # Initialize dp array with infinity
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting at step 0 has 0 cost

        for j in range(1, n + 1):
            # costs is 1-indexed in the problem description, so step j corresponds to costs[j - 1]
            step_cost = costs[j - 1]
            
            # You can jump from step i where i can be j - 1, j - 2, or j - 3
            for step in (1, 2, 3):
                i = j - step
                if i >= 0:
                    cost = dp[i] + step_cost + (step * step)
                    if cost < dp[j]:
                        dp[j] = cost

        return dp[n]