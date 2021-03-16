from typing import List
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(baseCosts)
        m = len(toppingCosts)
        # 可以任意组合吗
        # 这第一段代码写的真的狗屎关键还没有通过
        ans = baseCosts[0]
        for base in baseCosts:
            if abs(base-target) < abs(ans-target):
                ans = base

        toppingChose = set()
        # 选一种配料
        for topping in toppingCosts:
            toppingChose.add(topping)
            toppingChose.add(topping*2)

        # 选多种配料
        def chose(nums):
            # 从nums选出length个数来，返回所有的可能性
            if len(nums) >= 2:
                for i in range(len(nums)):
                    backtrace([], nums, i)
            elif len(nums) == 1:
                for num in nums:
                    toppingChose.add(num)
                    toppingChose.add(num*2)


        def backtrace(cur, path, length):
            if len(cur) == length:
                toppingChose.add(sum(cur))
            for i, p in enumerate(path):
                cur.append(p)
                tmp = path[:i]+path[i+1:]
                backtrace(cur, tmp, length)
                cur.pop()
                cur.append(p*2)
                backtrace(cur, tmp, length)
                cur.pop()
        toppingChose.add(0)
        chose(toppingCosts)
        for base in baseCosts:
            for item in toppingChose:
                if abs(base+item-target) < abs(ans-target):
                    ans = base+item
        return ans

    def closestCost2(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ret = baseCosts[0]
        for cost in toppingCosts:
            tmp = []
            for c in baseCosts:
                # 循环添加辅料和双倍辅料
                tmp.append(c + cost)
                tmp.append(c + 2 * cost)
            # 将本次遍历的总结果添加入baseCosts
            baseCosts.extend(tmp)
        # 上面这个过程就已经列举出所有的情况，关键我感觉我学不到这里代码的精髓啊，想不出来这么简洁的循环结构
        # 然后下面
        for i in baseCosts:
            if i == target:
                return target
            if abs(i - target) < abs(ret - target) or abs(i - target) == abs(ret - target) and i < ret:
                ret = i
        return ret

    def closestCost3(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        global ans
        ans = float('inf')

        def dfs(toppingCosts, target, sum_, k):
            global ans
            if abs(ans - target) > abs(target - sum_):
                ans = sum_
            if sum_ > target:
                return
            if k >= len(toppingCosts):
                return
            for i in range(3):
                dfs(toppingCosts, target, sum_ + i * toppingCosts[k], k+1)

        for i in baseCosts:
            dfs(toppingCosts, target, i, 0)
        return ans



if __name__ == '__main__':
    solu = Solution()
    baseCosts = [10]
    toppingCosts = [1]
    target = 1
    ans = solu.closestCost(baseCosts, toppingCosts, target)
    print(ans)