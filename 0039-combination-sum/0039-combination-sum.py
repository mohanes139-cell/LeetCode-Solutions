class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sorting helps prune branches early

        def backtrack(start: int, current_comb: list[int], remaining: int):
            if remaining == 0:
                res.append(list(current_comb))
                return

            for i in range(start, len(candidates)):
                # If the candidate exceeds the remaining sum, stop the loop
                # since candidates are sorted in ascending order
                if candidates[i] > remaining:
                    break

                current_comb.append(candidates[i])
                # Pass `i` (not `i + 1`) because the same element can be reused
                backtrack(i, current_comb, remaining - candidates[i])
                current_comb.pop()  # Backtrack

        backtrack(0, [], target)
        return res