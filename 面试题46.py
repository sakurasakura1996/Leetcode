"""
面试题46.把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""
# 感觉这个题目不难，但是有了想法之后我总是不知道该怎么编码，比如这道题，我一看到就有一个比较
# 直接的想法，就是创建一颗二叉树，然后有几个叶子节点其实就有几个解，但是但我编码的时候又不知道从哪下手了
# 后面自己打草稿想到一个广度优先的方法，这种BFS DFS的方法，遍历时并不需要先把树创建好才能遍历
# 那样会显得太麻烦。这里我用BFS，只用一个队列记录访问记录的索引就好了
from collections import deque
class Solution:
    def translateNum(self, num: int) -> int:
        if 0<=num<10:
            return 1
        # 先将num分离为个数，存入列表中
        nums = []
        while num!=0:
            tmp = num%10
            nums.insert(0,tmp)
            num = int(num/10)
        queue = deque()
        queue.append(0)
        if nums[0]*10 + nums[1] <= 25:
            queue.append(1)
        ans = 0
        while queue:
            idx = queue.popleft()
            if idx == len(nums)-1:
                ans += 1
            if idx+1<len(nums):
                queue.append(idx+1)
            if idx+2 < len(nums) and nums[idx+1]*10+nums[idx+2] <= 25 and nums[idx+1]!=0:
                queue.append(idx+2)
        return ans

# 上面的代码修改了很多次，有几种特殊情况我都没考虑到，这样下去不行啊
# way2
# 本题类似爬楼梯问题，只不过这一次爬两层楼梯是有条件的需要数字为10到25之间才可以然后根据这个条件递归就可以了
class Solution:
    def translateNum(self, num: int) -> int:
        if num<= 25 and num>=10:
            return 2
        elif num<10 or num < 100:
            return 1
        leftnum = num%100
        if leftnum <= 25 and leftnum >= 10:
            return self.translateNum(int(num/100)) + self.translateNum(int(num/10))
        else:
            return self.translateNum(int(num/10))
# 这个题解中看到的方法思路确实比我的好多了

# way3 这道题用动态规划方法还是比较容易想到的呀
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        if len(s) < 2:
            return 1
        dp = [0] * len(s)
        dp[0] = 1
        dp[1] = 2 if int(s[0] + s[1]) < 26 else 1
        for i in range(2,len(s)):
            dp[i] = dp[i-1] + dp[i-2] if int(s[i-1] + s[i]) < 26 and s[i-1] != '0' else dp[i-1]
        return dp[-1]




solu = Solution()
num = 12258
ans = solu.translateNum(num)
print(ans)






