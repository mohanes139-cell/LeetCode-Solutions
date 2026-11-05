class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If t is longer than s, it's impossible to form t
        if n > m:
            return 0
        
        # dp[j] represents the number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty target can always be formed 1 way
        
        for char_s in s:
            # Traverse backwards to use previous state values without extra space
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]