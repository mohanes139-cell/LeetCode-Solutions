class Solution:

  def minMoves(self, nums: list[int]) -> int:
    # Each move is equivalent to decrementing one element down towards min(nums)
    return sum(nums) - len(nums) * min(nums)