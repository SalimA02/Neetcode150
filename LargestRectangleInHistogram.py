class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []

        for x , y in enumerate(heights):
            start = x
            while stack and stack[-1][1] > y:
                sx, sy = stack.pop()
                maxArea = max(maxArea, sy * (x-sx))
                start = sx
            stack.append((start, y))

        for x, y in stack:
            maxArea =  max(maxArea, y * (len(heights) - x))

        return maxArea
