class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Place each number in its right place: nums[i] should be at nums[nums[i] - 1]
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Find the first index that doesn't contain i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all 1..n are present, the answer is n + 1
        return n + 1