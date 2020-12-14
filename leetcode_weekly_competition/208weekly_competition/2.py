from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        ans = []
        profit = 0
        customer = 0
        for i in range(n):
            customer += customers[i]
            if customer >=4:
                customer -= 4
                profit += 4 * boardingCost - runningCost
                ans.append(profit)
            else:

                profit += customer * boardingCost - runningCost
                customer = 0
                ans.append(profit)
        while customer > 0:
            if customer >= 4:
                customer -= 4
                profit += 4 * boardingCost - runningCost
                ans.append(profit)
            else:

                profit += customer * boardingCost - runningCost
                customer = 0
                ans.append(profit)
        max_profit = max(ans)
        if max_profit <= 0:
            return -1
        return ans.index(max_profit)+1

solu = Solution()
customers = [10,10,6,4,7]
boardingCost = 3
runningCost = 8
ans = solu.minOperationsMaxProfit(customers, boardingCost, runningCost)
print(ans)




