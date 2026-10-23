class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return

            # Prune branches that cannot provide enough remaining elements
            needed = k - len(path)
            for i in range(start, n - needed + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res