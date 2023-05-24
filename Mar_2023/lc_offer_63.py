import sys

class Solution:
    def maxProfit(self, prices) -> int:
        cost = sys.maxsize
        profit = 0
        for i, val in enumerate(prices):
            cost = min(val, cost)
            profit = max(val - cost, profit)
        return profit

    def maxProfit1(self, prices) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        cost = prices[0]
        for i, p in enumerate(prices[1:]):
            cost = min(p, cost)
            dp[i+1] = max(dp[i], p - cost)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2]
    s.maxProfit1(prices)