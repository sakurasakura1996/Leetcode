from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z'],
               }
        n = len(digits)
        if n == 0:
            return []
        if n == 1:
            return dic[digits]

        def merge(str1: List[str], str2: List[str]):
            ret = []
            for s1 in str1:
                for s2 in str2:
                    ret.append(s1+s2)
            return ret

        ans = merge(dic[digits[0]], dic[digits[1]])
        for i in range(2, n):
            ans = merge(ans, dic[digits[i]])
        return ans

    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrace(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrace(index+1)
                    combination.pop()
        combination = list()
        combinations = list()
        backtrace(0)
        return combinations


if __name__ == '__main__':
    solu = Solution()
    digits = "2"
    ans = solu.letterCombinations2(digits)
    print(ans)