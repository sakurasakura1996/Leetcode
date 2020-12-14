"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""
# 就模拟我们手工计算乘法的步骤，从后往前计算。相乘在相加
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        len1 = len(num1)
        len2 = len(num2)
        ans = ['0'] * (len1 + len2)
        flag = 0
        for i in range(len1):
            for j in range(len2):
                num = int(num1[-i-1]) * int(num2[-j-1])
                num = num + int(ans[i+j]) + flag
                flag = num // 10
                ans[i+j] = str(num%10)
            ans[i+len2] = str(flag)
            flag = 0
        ans.reverse()

        # return str(int(''.join(ans)))  这里使用了转换终究不是答案允许的
        target = ''.join(ans)
        for i,char in enumerate(target):
            if char == '0':
                ans = target[i+1:]
            else:
                ans = target[i:]
                break
        return ans

solu = Solution()
num1 = "9"
num2 = "9"
ans = solu.multiply(num1, num2)
print(ans)



