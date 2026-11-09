import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        # free_after stores available servers >= i % k
        # free_before stores available servers < i % k
        free_after = list(range(k))
        free_before = []
        
        # busy stores tuples of (end_time, server_id)
        busy = []
        
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            target = i % k

            # When starting a new circular round, shift any remaining servers
            # from free_after into free_before
            if target == 0:
                while free_after:
                    heapq.heappush(free_before, heapq.heappop(free_after))
                free_after, free_before = free_before, free_after

            # Release all servers that have finished before or at current arrival time
            while busy and busy[0][0] <= start:
                _, s_id = heapq.heappop(busy)
                if s_id >= target:
                    heapq.heappush(free_after, s_id)
                else:
                    heapq.heappush(free_before, s_id)

            # Assign request to next available server >= target, else wrap around to free_before
            if free_after:
                chosen = heapq.heappop(free_after)
            elif free_before:
                chosen = heapq.heappop(free_before)
            else:
                # All servers are busy; request is dropped
                continue

            count[chosen] += 1
            heapq.heappush(busy, (start + duration, chosen))

        max_req = max(count)
        return [idx for idx, c in enumerate(count) if c == max_req]