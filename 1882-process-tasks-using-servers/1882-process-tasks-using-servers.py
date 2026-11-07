import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Heap of available servers: (weight, index)
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # Heap of busy servers: (free_time, weight, index)
        busy_servers = []
        
        ans = []
        time = 0
        
        for i, task_time in enumerate(tasks):
            # Advance time to at least when task i arrives
            time = max(time, i)
            
            # If no servers are available, jump directly to when the earliest server frees up
            if not free_servers:
                time = max(time, busy_servers[0][0])
            
            # Release all servers that have finished their tasks by current time
            while busy_servers and busy_servers[0][0] <= time:
                free_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
            
            # Assign the best available server
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            heapq.heappush(busy_servers, (time + task_time, weight, idx))
            
        return ans