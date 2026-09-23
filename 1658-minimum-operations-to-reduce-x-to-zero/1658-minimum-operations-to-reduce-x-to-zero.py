class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        
        # If the target subarray sum is negative, it's impossible
        if target < 0:
            return -1
        # If target is 0, we must remove all elements
        if target == 0:
            return len(nums)
        
        left = 0
        current_sum = 0
        max_len = -1
        
        # Sliding window to find the longest subarray summing to target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1