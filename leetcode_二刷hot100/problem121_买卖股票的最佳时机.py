from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            ans = max(ans, prices[i] - min_price)
        return ans


if __name__ == '__main__':
    solu = Solution()
    prices = [7,6,4,3,1]
    ans = solu.maxProfit(prices)
    print(ans)
