from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 按照字典序倒序排序, 但是有个问题，就是 案例中的  30 和 3，
        # 直接倒序排序的时候，“30” > "3"，但是题目意思应该反过来。所以这样做是不行的，看了题解之后，发现这道题目以前我应该会做的啊。
        # 直接排序是不行的，我们如何判断两个数字的逻辑关系大小呢，按照这个题目的意思应该是 ： a, b, 如果 ab(拼接）< ba:那么应该就是 b > a
        nums = [str(num) for num in nums]
        nums.sort(reverse=True)  # sort排序的规则应该可以重新定义
        return "".join(nums)

    def largestNumber2(self, nums: List[int]) -> str:
        # 上面的方法不对啊，不能应对该题目中 30 和 3要求的大小关系。
        # 用冒泡排序？肯定可行，但是不是显得麻烦，我后来百度了下，python 的sort() 和 sorted()都没有cmp 参数了，原来python2是有的
        # 我们可以用 functools.cmp_to_key() 将python2风格的cmp函数转换为key的函数
        def compare(x, y):
            if int(str(x)+str(y)) < int(str(y)+str(x)):
                return -1
            elif int(str(x)+str(y)) > int(str(y)+str(x)):
                return 1
            return 0
        nums.sort(key=cmp_to_key(compare), reverse=True)
        nums = [str(num) for num in nums]
        return str(int("".join(nums)))   # 为了应对 [0,0]这种返回 “00”的错误。


if __name__ == '__main__':
    solu = Solution()
    nums = [3,30,34,5,9]
    ans = solu.largestNumber2(nums)
    print(ans)