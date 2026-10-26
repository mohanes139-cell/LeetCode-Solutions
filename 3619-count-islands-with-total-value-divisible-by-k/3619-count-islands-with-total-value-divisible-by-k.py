from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for r in range(m):
            for c in range(n):
                # If we encounter unvisited land (positive integer)
                if grid[r][c] > 0:
                    total_val = 0
                    queue = deque([(r, c)])
                    total_val += grid[r][c]
                    grid[r][c] = 0  # Mark visited by setting to 0
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                total_val += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark visited
                                queue.append((nr, nc))
                    
                    if total_val % k == 0:
                        count += 1
                        
        return count