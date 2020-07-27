"""
1323. 6 和 9 组成的最大数字
给你一个仅由数字 6 和 9 组成的正整数 num。
你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
请返回你可以得到的最大数字。
示例 1：
输入：num = 9669
输出：9969
解释：
改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。
改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。
其中最大的数字是 9969 。
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = []
        while num:
            cur = num % 10
            num = num // 10
            ans.append(cur)
        ans_num = 0
        while ans:
            cur = ans.pop()
            if cur == 6:
                ans_num = ans_num*10 + 9
                break
            else:
                ans_num = ans_num * 10 + cur
        while ans:
            cur = ans.pop()
            ans_num = ans_num * 10 + cur
        return ans_num

    def maximum69Number(self, num:int) -> int:
        # 妈的，还是不熟悉python的写法啊
        return int(str(num).replace('6','9',1))


solu = Solution()
ans = solu.maximum69Number(9999)
print(ans)