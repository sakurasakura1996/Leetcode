"""
剑指 Offer 44. 数字序列中某一位的数字
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
示例 1：
输入：n = 3
输出：3
示例 2：
输入：n = 11
输出：0
限制：
0 <= n < 2^31
注意：本题与主站 400 题相同
"""
class Solution:
    def findNthDigit(self, n:int) -> int:
        # 此方法超时，这种方法实在太蠢了。
        cur = 0
        ans = []
        num = 0
        while cur < n+1:
            item = str(num)
            item_len = len(item)
            ans.extend(list(item))
            cur += item_len
            num += 1
        print(ans)
        return int(ans[n])

    def findNthDigit2(self, n: int) -> int:
        



if __name__ == '__main__':
    solu = Solution()
    n = 11
    ans = solu.findNthDigit(n)
    print(ans)