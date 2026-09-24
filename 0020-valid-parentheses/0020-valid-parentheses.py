class Solution:
    def isValid(self, s: str) -> bool:
        # A valid string must have an even number of characters
        if len(s) % 2 != 0:
            return False

        # Map closing brackets to their corresponding opening brackets
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if char in matching:
                # If stack is non-empty, pop the top element; otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                if matching[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0