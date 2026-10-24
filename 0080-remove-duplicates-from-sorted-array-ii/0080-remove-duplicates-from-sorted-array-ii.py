class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # k points to the index where the next valid element should be placed
        k = 2
        for i in range(2, len(nums)):
            # If the current number is different from the number 2 positions back,
            # it means we have not yet included more than two duplicates of it.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k