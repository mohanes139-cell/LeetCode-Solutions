class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1        # Pointer for the last valid element in nums1
        p2 = n - 1        # Pointer for the last element in nums2
        p = m + n - 1     # Pointer for the write position at the end of nums1

        # Compare elements from the back and place the larger one at the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy any remaining elements from nums2
        # (If p1 >= 0 elements remain, they are already in their correct sorted places)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1