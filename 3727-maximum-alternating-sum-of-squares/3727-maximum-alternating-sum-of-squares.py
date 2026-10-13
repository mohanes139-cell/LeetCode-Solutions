class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        m = len(nums) // 2
        
        # Subtract the m smallest squares, add the rest
        return sum(squares[m:]) - sum(squares[:m])