from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        m = (x + 1) // 2  # Size of lower half (including median)
        
        # Maintain sliding window elements using SortedList
        sl = SortedList()
        sum_left = 0
        sum_right = 0
        
        costs = [0] * n  # costs[i] = cost to make window nums[i - x + 1 .. i] equal
        
        for i in range(n):
            val = nums[i]
            
            # 1. Add current element nums[i]
            # Find where val lands relative to the split point m - 1
            idx = sl.bisect_left(val)
            if len(sl) < m:
                sum_left += val
            else:
                if idx < m:
                    # An element from left moves to right
                    migrating = sl[m - 1]
                    sum_left += val - migrating
                    sum_right += migrating
                else:
                    sum_right += val
            sl.add(val)
            
            # 2. Remove outgoing element nums[i - x]
            if i >= x:
                out_val = nums[i - x]
                out_idx = sl.index(out_val)
                if out_idx < m:
                    # An element from right moves to left
                    if len(sl) > m:
                        migrating = sl[m]
                        sum_left += migrating - out_val
                        sum_right -= migrating
                    else:
                        sum_left -= out_val
                else:
                    sum_right -= out_val
                sl.remove(out_val)
            
            # 3. Calculate cost for window of size x ending at i
            if i >= x - 1:
                median = sl[m - 1]
                # Elements in left half <= median, elements in right half >= median
                if x % 2 == 1:
                    # sum_left includes median once:
                    # cost = sum_right - (sum_left - median)
                    costs[i] = sum_right - sum_left + median
                else:
                    # |left| == |right| == x // 2
                    costs[i] = sum_right - sum_left
        
        # DP: dp[j] = min cost choosing j non-overlapping windows of length x
        INF = float('inf')
        dp = [0] + [INF] * k
        
        # To handle non-overlapping condition with length x,
        # we can record the history of dp at each step
        dp_history = [dp[:]]
        
        for i in range(n):
            new_dp = list(dp_history[-1])
            if i >= x - 1:
                prev_dp = dp_history[i - x + 1]
                c = costs[i]
                for j in range(1, k + 1):
                    if prev_dp[j - 1] != INF:
                        new_dp[j] = min(new_dp[j], prev_dp[j - 1] + c)
            dp_history.append(new_dp)
        
        return dp_history[-1][k]