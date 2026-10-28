class Solution:

  def minCost(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # dp[c] stores a set of all reachable XOR values at column c
    # dp[c] is initialized with sets of reachable values
    dp = [set() for _ in range(n)]

    # Base case: top-left cell
    dp[0].add(grid[0][0])

    # Initialize first row
    for c in range(1, n):
      val = grid[0][c]
      dp[c] = {x ^ val for x in dp[c - 1]}

    # Process remaining rows
    for r in range(1, m):
      # First column can only come from above
      val = grid[r][0]
      dp[0] = {x ^ val for x in dp[0]}

      for c in range(1, n):
        val = grid[r][c]
        # Can transition from top (dp[c]) or left (dp[c - 1])
        dp[c] = {x ^ val for x in (dp[c] | dp[c - 1])}

    # The result is the minimum XOR value reachable at (m - 1, n - 1)
    return min(dp[n - 1])