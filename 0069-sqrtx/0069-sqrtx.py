class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 1

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                ans = mid       # mid is a valid floor candidate
                left = mid + 1  # search for a larger integer
            else:
                right = mid - 1 # mid^2 is too large

        return ans