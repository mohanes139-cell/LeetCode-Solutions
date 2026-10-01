class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' has no matching '(', reset the base index
                    stack.append(i)
                else:
                    # Valid substring spans from stack[-1] to i
                    max_len = max(max_len, i - stack[-1])

        return max_len