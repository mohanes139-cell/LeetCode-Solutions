class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        def backtrack(index: int, current_path: list[str]) -> None:
            # Base case: completed a valid combination
            if index == len(digits):
                combinations.append("".join(current_path))
                return

            # Explore all possible letters for the current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                current_path.append(letter)
                backtrack(index + 1, current_path)
                current_path.pop()  # Backtrack

        backtrack(0, [])
        return combinations