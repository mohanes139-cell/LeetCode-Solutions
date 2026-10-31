from functools import lru_cache

class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dir_in: 0 = moving Right, 1 = moving Down
        @lru_cache(maxsize=None)
        def get_destination(r: int, c: int, dir_in: int):
            if not (0 <= r < m and 0 <= c < n):
                return None
            
            # Destination cell is always an end state if reached
            if (r, c) == (m - 1, n - 1):
                return (r, c)
            
            if grid[r][c] == 0:
                return (r, c)
            
            # Reflected by mirror
            if dir_in == 0:
                # Arrived moving Right -> turned Down
                return get_destination(r + 1, c, 1)
            else:
                # Arrived moving Down -> turned Right
                return get_destination(r, c + 1, 0)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                count = dp[r][c]
                if count == 0 or grid[r][c] == 1:
                    continue
                
                # Try moving Right (dir_in = 0)
                dest_right = get_destination(r, c + 1, 0)
                if dest_right is not None:
                    nr, nc = dest_right
                    dp[nr][nc] = (dp[nr][nc] + count) % MOD
                
                # Try moving Down (dir_in = 1)
                dest_down = get_destination(r + 1, c, 1)
                if dest_down is not None:
                    nr, nc = dest_down
                    dp[nr][nc] = (dp[nr][nc] + count) % MOD

        return dp[m - 1][n - 1]