class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []

        def backtrack(start: int, parts: list[str]):
            # If we already have 4 parts, check if the entire string was consumed
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return

            # Each segment can be 1 to 3 characters long
            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start : start + length]

                # Disallow leading zeros for numbers with 2 or more digits
                if len(segment) > 1 and segment[0] == "0":
                    break

                # Segment must be between 0 and 255
                if int(segment) <= 255:
                    backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return res