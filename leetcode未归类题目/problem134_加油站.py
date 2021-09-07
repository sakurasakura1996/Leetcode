from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas = gas + gas
        cost = cost + cost
        for i in range(n):
            # 起始加油站点
            start = i
            gass = gas[start]
            costt = cost[start]
            num = 0  # 记录走过的加油站数量
            while gass >= costt:
                if num >= n:
                    return i
                start += 1
                gass += gas[start]
                gass -= costt
                costt = cost[start]
                num += 1
        return -1


if __name__ == '__main__':
    solu = Solution()
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    ans = solu.canCompleteCircuit(gas, cost)
    print(ans)