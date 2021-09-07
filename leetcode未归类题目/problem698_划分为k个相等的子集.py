from typing import List
from collections import Counter
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 头晕了的自己，改代码写错了啊，感觉还是得回溯。
        summ = sum(nums)
        if summ % k != 0:
            return False
        target = summ // k
        nums_counter = Counter(nums)
        for num in nums:   # 这样写，怕不是你人晕了啊，难道只能是两个元素拼接成target吗 哈哈哈。
            if num > target:
                return False
            elif num == target:
                nums_counter[num] -= 1
            elif num < target and target - num in nums_counter and nums_counter[target-num]>0:
                nums_counter[num] -= 1
                nums_counter[target - num] -= 1
        for key, value in nums_counter.items():
            if value != 0:
                return False
        return True

    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        # 回溯法,思路是模拟构造 k 个子集(nums的不相交子集).对于nums中每个数字，我们将其
        # 放入第i个子集检查是否解决了问题，我们可以通过递归搜索来检查是否存在可能性。
        # 注意看题目中的提示， nums的长度最长为16，说明递归是一个通用解法啊
        if k == 1:
            return True
        summ = sum(nums)
        if summ % k != 0:
            return False
        target = summ // k

        def backtrace(groups):
            if not nums:
                return True
            # 向下递归，选择数字，看放在哪个篮子里面，
            v = nums.pop()
            for i in range(k):
                # 思考一下，如果所有子集都能做到 子集和 <= target，那么其实他们都等于target了。哈哈哈
                if groups[i] + v <= target:
                    groups[i] += v
                    if backtrace(groups):
                        return True
                    # 返回重置状态
                    groups[i] -= v
                # 细节问题，减少重复搜索，保证0始终在末尾
                # 这里的细节问题什么意思要好好理解下。这个不加会超时。
                # 因为来了一个数，groups前面的数加上都不行了，所以才轮到这个数的，我们只要维持groups末尾的0，
                # 遇到0的时候，说明groups后面的元素都是0，前面执行了加v的操作，结果到了这里，没有返回true，说明
                # 等于0不行啊，那把这个v加到后面的0上肯定还是不行的啊，那优化下，就直接放弃这种搜索了啊
                if groups[i] == 0:
                    break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target:
            return False
        # while nums and nums[-1] == target:
        #     nums.pop()
        #     k -= 1
        # 如果剩下的全是0，也是return True
        # 不加下面这一句是错误的。比如[8,8,0]这种情况，主要还是因为上面nums[-1] == target直接去掉的问题。
        # 如果不加上面的判断，是没问题的。但是效率总体还是低些
        # if not any(nums):
        #     return True
        return backtrace([0] * k)




if __name__ == '__main__':
    solu = Solution()
    nums = [8, 8, 0]
    k = 2
    ans = solu.canPartitionKSubsets2(nums, k)
    print(ans)



