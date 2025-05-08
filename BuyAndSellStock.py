class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0 

        for i in range(len(prices)-1):
            maximumProfit = max((max(prices[i+1:])- prices[i]), maximumProfit)

        return maximumProfit
#2P

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
