class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Check cyclic monotonicity
        is_inc = True
        is_dec = True
        for j in range(n):
            if nums[(j + 1) % n] != (nums[j] + 1) % n:
                is_inc = False
            if nums[(j + 1) % n] != (nums[j] - 1 + n) % n:
                is_dec = False

        if not is_inc and not is_dec:
            return -1

        i = nums.index(0)

        ans = float("inf")
        if is_inc:
            ans = min(ans, i, (n - i) % n + 2)
        if is_dec:
            ans = min(ans, n - i, (i + 1) % n + 1)

        return ans