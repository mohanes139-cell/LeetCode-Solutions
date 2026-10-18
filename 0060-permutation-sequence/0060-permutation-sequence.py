import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based index
        fact = math.factorial(n - 1)
        res = []

        for i in range(n - 1, 0, -1):
            index = k // fact
            res.append(numbers.pop(index))
            k %= fact
            fact //= i  # Equivalent to math.factorial(i - 1)

        res.append(numbers[0])  # Append the last remaining number
        return "".join(res)