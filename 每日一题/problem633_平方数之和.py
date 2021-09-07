import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 这种问题，如果直接用暴力法应该是肯定通过不了的啊, c的范围到达 2 ^ 31方，太大了吧
        # 想想看有没有其他的解决方法啊
        # 如果用暴力法的话，从1开始算起，到 c/2再开根号这么大
        # 卧槽，暴力方法竟然搞定了。。
        low = 0
        high = int(math.sqrt(c//2))
        for i in range(low, high+1):
            cur = math.sqrt(c - i * i)
            if cur == int(cur):
                return True
        return False

    def judgeSquareSum2(self, c: int) -> bool:
        # 题解中还有双指针方法：
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            sum = left * left + right * right
            if sum == c:
                return True
            elif sum < c:
                left += 1
            else:
                right -= 1
        return False

if __name__ == '__main__':
    solu = Solution()
    c = 1
    ans = solu.judgeSquareSum(c)
    print(ans)


