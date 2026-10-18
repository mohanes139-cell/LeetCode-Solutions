class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row with 1s (only 1 way to go strictly right)
        row = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]

        return row[-1]