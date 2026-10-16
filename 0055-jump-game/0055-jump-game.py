class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)
        
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= n - 1:
                return True
                
        return True