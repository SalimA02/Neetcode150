class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            lMax = Max = height[i]

            for j in range(i):
                lMax = max(lMax, height[j])
            for j in range(i + 1, n):
                Max = max(Max, height[j])
                
            res += min(lMax, Max) - height[i]
        return res
