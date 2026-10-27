class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # If total operations cover the entire sum of differences, we can reduce all to 0
        if sum(diffs) <= k:
            return 0
        
        # Count frequencies of each difference value
        max_diff = max(diffs)
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        # Greedily reduce from the largest difference downwards
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
                
            if k >= count[d]:
                # Decrement all elements of size d to d - 1
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                # Can only decrement k of the elements of size d
                count[d] -= k
                count[d - 1] += k
                k = 0
                break

        # Compute the resulting sum of squared differences
        return sum(c * (d ** 2) for d, c in enumerate(count))