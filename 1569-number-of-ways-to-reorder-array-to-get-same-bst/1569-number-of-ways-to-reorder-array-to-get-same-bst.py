from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            # Interleave left and right elements, then recurse
            ways = comb(len(left) + len(right), len(left)) * dfs(left) * dfs(right)
            return ways % MOD

        # Subtract 1 to exclude the original arrangement
        return (dfs(nums) - 1) % MOD