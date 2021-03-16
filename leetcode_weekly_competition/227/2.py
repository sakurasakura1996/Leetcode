
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 每次取的三个数中最大的两个是最稳妥的吧
        ans = 0
        nums = [a, b, c]
        while (nums[0] and nums[1]) or (nums[0] and nums[2]) or (nums[1] and nums[2]):
            nums.sort()
            nums[1] -= 1
            nums[2] -= 1
            ans += 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    a = 1
    b = 8
    c = 8
    ans = solu.maximumScore(a, b, c)
    print(ans)

