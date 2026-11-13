from collections import deque


class Solution(object):

    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        # Stores [value, count] in strictly decreasing order of value
        dq = deque()

        for l in range(n - 1, -1, -1):
            val = nums[l]
            cnt = 1

            # Merge all front blocks smaller than or equal to the new left element
            while dq and dq[0][0] <= val:
                prev_val, prev_cnt = dq.popleft()
                cost += prev_cnt * (val - prev_val)
                cnt += prev_cnt

            dq.appendleft([val, cnt])

            # Shrink window from the right until total operations <= k
            while cost > k:
                # The rightmost element's required target height is dq[-1][0]
                cost -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans