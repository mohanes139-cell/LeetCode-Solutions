import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            # If idx is within bounds and arr2[idx] <= x + d, then arr2[idx] is in [x - d, x + d]
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
            count += 1
            
        return count