import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # Every subarray of length 2 satisfies a * b == lcm(a, b) * gcd(a, b)
        max_len = 2
        # Maximum possible LCM for numbers in range [1, 10] is lcm(1..10) = 2520
        MAX_LCM = 2520

        for i in range(n):
            curr_prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                curr_prod *= nums[j]
                if curr_prod > MAX_LCM:
                    break

                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])

                if curr_prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)

        return max_len