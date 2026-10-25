class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights: list[int]) -> int:
            stack = []
            max_row_area = 0
            extended = heights + [0]

            for i, h in enumerate(extended):
                while stack and extended[stack[-1]] > h:
                    height = extended[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_row_area = max(max_row_area, height * width)
                stack.append(i)

            return max_row_area

        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area