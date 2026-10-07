from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True

            # If a valid string has been found at this level,
            # do not generate deeper levels (which have more removals).
            if found:
                continue

            # Generate all possible next states by removing one parenthesis
            for i, char in enumerate(curr):
                if char not in ('(', ')'):
                    continue
                
                # Avoid generating duplicate states from consecutive identical parentheses
                if i > 0 and curr[i] == curr[i - 1]:
                    continue

                nxt = curr[:i] + curr[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result