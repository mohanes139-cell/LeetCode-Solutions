class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize dp with the first row's prefix sums
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
            
        # Process the remaining rows
        for i in range(1, m):
            dp[0] += grid[i][0]  # First column can only come from above
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
                
        return dp[-1]