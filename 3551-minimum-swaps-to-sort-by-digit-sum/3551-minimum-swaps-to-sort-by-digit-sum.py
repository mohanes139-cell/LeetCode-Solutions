class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def get_digit_sum(val: int) -> int:
            s = 0
            while val > 0:
                s += val % 10
                val //= 10
            return s

        # Pair each number with its digit sum
        # nums has distinct positive integers
        digit_sums = [get_digit_sum(x) for x in nums]

        # Target sorted order: primary key = digit sum, secondary key = value
        target = sorted(range(n), key=lambda i: (digit_sums[i], nums[i]))

        # Map each index to where it needs to go
        # target[i] is the original index of the element that should end up at position i
        pos = [0] * n
        for i, orig_idx in enumerate(target):
            pos[orig_idx] = i

        # Count cycles in the permutation
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[i] == i:
                continue

            cycle_len = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = pos[curr]
                cycle_len += 1

            if cycle_len > 1:
                swaps += cycle_len - 1

        return swaps