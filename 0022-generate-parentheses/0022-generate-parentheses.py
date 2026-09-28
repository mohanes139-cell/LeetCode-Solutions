class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: valid combination complete
            if len(current) == 2 * n:
                res.append(current)
                return

            # Can place an open parenthesis if count is less than n
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Can only place a close parenthesis if there are unmatched open ones
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res