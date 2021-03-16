"""
338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。
示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]
进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""
# 看起来不难的一道题，可以用的方法十分多，具体分析见语雀笔记。
from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        for i in range(num+1):
            tmp = bin(i)
            ans.append(tmp.count('1'))
        return ans

    def countBits2(self, num: int) -> List[int]:
        # 先看看如果不使用上面python提供的内置函数，先不看能否满足时间空间复杂度，这里记录一个计算单个数二进制1的个数的方法
        def bin_counts(n):
            count = 0
            while n:
                n &= n-1
                count += 1
            return count
        ans = []
        for i in range(num+1):
            ans.append(bin_counts(i))
        return ans


    def countBits3(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ans = [0]
        dic = {0: 0}
        for i in range(1, num+1):
            if i & (i-1) == 0:  # i的二进制形式为 10000，i-1为1111，所以两者想与就是0了。
                pre = i   # 这里的方法还挺巧妙的 后面的else中需要用到pre，比如  10111的pre是10000
                count = 1
            else:
                count = 1+dic[i-pre]
            dic[i] = count
            ans.append(count)
        return ans


    def countBits4(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        for i in range(1, num+1):
            dp[i] = dp[i&(i-1)] + 1   # 这里的表达很巧妙啊  # 如果 i二进制末尾为0，i-1二进制末尾为1                        # 如果 i二进制末尾为1, i-1二进制末尾为0
        return dp

    def countBits5(self, num: int) -> List[int]:
        # 分奇偶来做
        dp = [0] * (num+1)
        for i in range(1, num+1):
            if i%2:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i//2]
        return dp

## 如果i的二进制 & i-1 的二进制  == 0: 那么这个i的格式为  10000...
## 如果  i & (i-1) 得到的结果是把i的二进制表示中最末尾的1给置为0之后的数的结果。


if __name__ == '__main__':
    solu = Solution()
    num = 5
    ans = solu.countBits5(num)
    print(ans)
