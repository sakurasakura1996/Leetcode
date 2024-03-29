"""
剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""
# 先判断是否有e或者E，有的话，前后分成两半，前面必须是数，后面必须是整数。
# 如果没有e和E的话，那么就必须是一个数。
# 判断是否是一个数，有+ - 和 .等。
class Solution:
    def isNumber(self, s: str) -> bool:
        

        def isZhengshu(num: str):
            # 判断字符串num是否是整数，包括正负符号
            if not num:
                return False
            n = len(num)
            if num[0] == '+' or num[0] == '-':
                if n == 1:
                    return False
                else:
                    for i in range(1, n):
                        if not num[i].isdigit():
                            return False
                    return True
            else:
                for i in range(n):
                    if not num[i].isdigit():
                        return False
                return True

        def

