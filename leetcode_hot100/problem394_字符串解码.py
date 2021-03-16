"""
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""
# 因为题目说 输入字符串总是有效的，且原始数据不包含数字。所有的数字只表示重复的次数k
class Solution:
    def decodeString(self, s: str) -> str:
        # 下面的解法明显错误了，我们完全没考虑到括号嵌套的问题，所以嵌套要用栈啊，下面的代码错了哈
        if not s:return s
        ans = ""
        n = len(s)
        print(n)
        cur = 0
        tmp = ""
        for i in range(n):
            if s[i] >= '0' and s[i] <= '9':
                cur = int(s[i]) + cur * 10
            elif s[i] == '[':
                tmp = ""
            elif s[i] == ']':
                ans = ans + (tmp * cur)
                cur = 0
            else:
                tmp += s[i]
        return ans

    def decodeString2(self, s: str) -> str:
        if not s:return s
        stack = []
        n = len(s)
        cur = 0
        tmp = ""
        for i in range(n):
            if s[i] == '[':
                stack.append(str(cur))
                cur = 0
            elif s[i] >= '0' and s[i] <= '9':
                if tmp:
                    stack.append(tmp)
                    tmp = ""
                cur = cur * 10 + int(s[i])
            elif s[i] == ']':
                # tmp为当前字符部分，出栈一个数字即可
                while not stack[-1].isdigit():
                    tmp = stack.pop() + tmp
                num = stack.pop()
                stack.append(tmp * int(num))
                tmp = ""
            else:
                tmp += s[i]
        ans = ""
        while stack:
            ans = stack.pop() + ans
        return ans + tmp


    def decodeString3(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "abc3[cd]xyz"
    ans = solu.decodeString2(s)
    print(ans)