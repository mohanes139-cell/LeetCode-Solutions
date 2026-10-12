class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap current element with element at index i
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse for the next position
                backtrack(start + 1)
                # Backtrack / restore original array state
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return result