"""
415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 这方法写的不漂亮，可以把短的字符串前面附上0
        num1 = list(num1)
        num2 = list(num2)
        num1_len = len(num1)
        num2_len = len(num2)
        flag = 0
        ans = []
        i = 1
        while i <= num1_len and i <= num2_len:
            num = flag+int(num1[-i])+int(num2[-i])
            flag = num//10
            ans.insert(0, str(num%10))
            i += 1
        if num1_len < num2_len:
            # 把num2的部分放入ans中
            while i <= num2_len:
                num = flag + int(num2[-i])
                flag = num//10
                ans.insert(0, str(num%10))
                i += 1
        else:
            while i <= num1_len:
                num = flag + int(num1[-i])
                flag = num//10
                ans.insert(0, str(num%10))
                i += 1
        if flag > 0:
            ans.insert(0,str(flag))
        return ''.join(ans)

# 这个大佬写的方法就简洁高效了很多啊。多学习学习
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res




