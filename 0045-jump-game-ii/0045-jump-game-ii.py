class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to check the last index because once we reach or pass it, we are done.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # Reached the boundary of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if we can already reach or exceed the last index
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps