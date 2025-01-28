class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)

        output = 0

        r = length - 1
        for l in range(r):
            for j in range(r, l, -1):
                current = min(heights[l], heights[j]) * (j-l)
                output = max(output, current)
        return output
