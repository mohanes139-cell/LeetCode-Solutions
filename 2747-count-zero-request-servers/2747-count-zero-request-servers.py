from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda log: log[1])
        
        # Keep track of original indices: (query_time, original_index)
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        
        left = 0
        right = 0
        m = len(logs)
        
        for orig_idx, q_time in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand window: add logs occurring at or before q_time
            while right < m and logs[right][1] <= window_end:
                server_counts[logs[right][0]] += 1
                right += 1
                
            # Shrink window: remove logs occurring before q_time - x
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left += 1
                
            # Number of inactive servers = total - unique active servers
            ans[orig_idx] = n - len(server_counts)
            
        return ans