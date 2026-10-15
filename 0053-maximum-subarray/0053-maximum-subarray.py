class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_so_far = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            # Either extend the previous subarray or start fresh from num
            current_sum = max(num, current_sum + num)
            max_so_far = max(max_so_far, current_sum)
            
        return max_so_far