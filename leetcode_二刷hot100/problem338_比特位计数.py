# 这道题考察了一个很重要的知识点：但是不好记住： x = x&(x-1) 这个运算操作将x的二进制表示的最后一个1变成了0，因此对x重复操作，就知道有多少个1了。
# 同理，我们可以用递归或者动态规划来写这个问题，只将该运算进行一次 ，通过dp[x&(x-1)]+1来得到dp[x]的值即可啦
from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        # 使用python内置函数很简单
        ans = []
        for i in range(num+1):
            ans.append(bin(i).count('1'))
        return ans

    def countBits2(self, num: int) -> List[int]:
        # 题目要求在线性时间O（n）内用一趟扫描做到，空间复杂度也是O（n），然后不使用语言的内置函数
        # 这道题目中的规律或者说知识点，我还是没记住，主要就是 我们通过 i-1 和 i的二进制与的结果来做
        # 我们知道了如果i-1的二进制末尾为0，则i的二进制末尾为1，且前面部分都是一样的，那么dp[i] = dp[i-1] + 1
        # 那么如果 i-1二进制末尾为1，则结果就不一样了。就是这里不太好想通，我们可以一步一步来，先写一个函数来求得一个数的二进制中1的个数
        def bin_counts(n):
            count = 0
            # 我们来看看这个函数过程，其实思路就出来了，这里有一点像递归的感觉，
            while n:
                n &= n-1
                count += 1
            return count
        ans = []
        for i in range(num+1):
            ans.append(bin_counts(i))
        return ans






if __name__ == '__main__':
    solu = Solution()
    ans = solu.countBits(5)
    print(ans)