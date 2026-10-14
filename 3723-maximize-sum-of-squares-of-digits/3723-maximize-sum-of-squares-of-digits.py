class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Maximum possible sum for `num` digits is 9 * num
        # The sum cannot be less than 1 for a positive integer
        if sum > 9 * num or sum < 1:
            return ""
        
        # Greedily take as many 9s as possible
        count_9 = sum // 9
        remainder = sum % 9
        
        digits = ["9"] * count_9
        
        if remainder > 0:
            digits.append(str(remainder))
            
        # Pad with trailing 0s to reach exactly `num` digits
        remaining_zeros = num - len(digits)
        if remaining_zeros < 0:
            return ""
            
        digits.append("0" * remaining_zeros)
        
        return "".join(digits)