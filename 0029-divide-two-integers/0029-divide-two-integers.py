class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit signed integer limits
        MAX_INT = 2147483647      # 2^31 - 1
        MIN_INT = -2147483648     # -2^31

        # Handle overflow edge case: -2^31 / -1 = 2^31 (exceeds MAX_INT)
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Bitwise exponential subtraction
        while a >= b:
            temp_b = b
            multiple = 1
            # Double temp_b and multiple using left-shift until it exceeds a
            while a >= (temp_b << 1):
                temp_b <<= 1
                multiple <<= 1
            
            a -= temp_b
            quotient += multiple

        result = -quotient if negative else quotient

        # Clamp within the 32-bit signed integer range
        return max(MIN_INT, min(MAX_INT, result))