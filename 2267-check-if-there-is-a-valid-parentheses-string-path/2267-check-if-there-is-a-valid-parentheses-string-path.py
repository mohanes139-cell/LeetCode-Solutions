from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_steps = m + n - 1
        
        # Necessary conditions
        if total_steps % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        max_open = total_steps // 2

        @lru_cache(None)
        def dfs(r: int, c: int, bal: int) -> bool:
            # Update running balance
            bal += 1 if grid[r][c] == '(' else -1
            
            # Prune invalid paths
            if bal < 0 or bal > max_open:
                return False
            
            # Remaining steps left to reach destination
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if bal > remaining_steps:
                return False
            
            # Reached target cell
            if r == m - 1 and c == n - 1:
                return bal == 0
            
            # Explore down and right
            if r + 1 < m and dfs(r + 1, c, bal):
                return True
            if c + 1 < n and dfs(r, c + 1, bal):
                return True
            
            return False

        return dfs(0, 0, 0)