class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                # If already included in current path, skip
                if used[i]:
                    continue
                # If current element is duplicate of previous and previous was skipped in this level, skip
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
                
        backtrack()
        return res