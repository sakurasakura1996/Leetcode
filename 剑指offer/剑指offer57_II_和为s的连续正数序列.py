from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 为啥用python刷题感觉思路就来了呢。。我在想是否可以用滑动窗口来做啊
        # 因为是连续序列，所以，就应该要想到是否可以用滑动窗口或者说是双指针解法
        left = 1
        right = 2
        ans = []
        window = 1
        while right < target:
            window += right
            right += 1
            while window > target:
                window -= left
                left += 1
            if window == target:
                ans.append([i for i in range(left, right)])
        return ans

    def findContinuousSequence2(self, target: int) -> List[List[int]]:
        ans = []

        def backtrace(cur, idx, summ):
            if summ == target:
                ans.append(cur.copy())
                return
            # 连续的数字序列，所以只需要加上后面一个
            if summ + idx > target:
                return
            else:
                cur.append(idx)
                idx += 1
                backtrace(cur, idx, summ + idx - 1)
                return
        # 这道题不应该用回溯方法来写，这尼玛不就是暴力，写的还贼麻烦
        for i in range(1, target):
            backtrace([], i, 0)
        return ans

if __name__ == '__main__':
    solu = Solution()
    ans = solu.findContinuousSequence2(15)
    print(ans)


