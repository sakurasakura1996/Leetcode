"""
709. 转换成小写字母
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
示例 1：
输入: "Hello"
输出: "hello"

示例 2：
输入: "here"
输出: "here"

示例 3：
输入: "LOVELY"
输出: "lovely"
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

    def toLowerCase_2(self, str:str) -> str:
        dic = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
               'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
               'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
               'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
               'Y': 'y', 'Z': 'z'}

        ans = []
        for i in str:
            if i in dic:
                ans.append(dic[i])
            else:
                ans.append(i)
        return ''.join(ans)


solu = Solution()
print(solu.toLowerCase("LoVye"))