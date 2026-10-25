class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # stores indices
        max_area = 0
        # Append 0 to flush out all remaining bars in the stack at the end
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, it extends all the way to index 0 (width = i)
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # restore original array
        return max_area