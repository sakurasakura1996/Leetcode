""""
696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。
示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
请注意，一些重复出现的子串要计算它们出现的次数。
另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：
s.length 在1到50,000之间。
s 只包含“0”或“1”字符。
"""
class Solution:
    # 此方法超时报错
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        ans = 0

        def check(s):
            if not s:
                return False
            m = len(s)
            if m%2==1:return False
            str1 = '0' * (m//2) + '1' * (m//2)
            str2 = '1' * (m//2) + '0' * (m//2)
            if s == str1 or s == str2:
                return True
        for i in range(n):
            for j in range(i,n+1):
                if check(s[i:j]):
                    ans += 1
                    break
        return ans

    def countBinarySubstrings_2(self, s: str) -> int:
        # 我们可以发现，只需要将s中连续的字符个数统计放入数组中，然后两两比较最小值加入答案中
        ans = 0
        last = ''
        j=k=0
        for i in s:
            if last == i:
                j += 1
            else:
                last = i
                ans += min(j,k)
                k,j = j,1
        return ans + min(j,k)

    def countBinarySubstring_3(self, s:str)->int:
        nums = []
        temp = s[0]
        count = 0
        for i in s:
            if i == temp:
                count += 1
            else:
                nums.append(count)
                temp = i
                count = 1
        nums.append(count)
        ans = 0
        for i in range(1,len(nums)):
            ans += min(nums[i-1], nums[i])
        return ans

solu = Solution()
s = "00110011"
ans = solu.countBinarySubstrings(s)
print(ans)