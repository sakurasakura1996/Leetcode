"""
1208.尽可能使字符串相等
给你两个长度相同的字符串，s 和 t。
将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
示例 1：
输入：s = "abcd", t = "bcdf", cost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。

示例 2：
输入：s = "abcd", t = "cdef", cost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。

示例 3：
输入：s = "abcd", t = "acde", cost = 0
输出：1
解释：你无法作出任何改动，所以最大长度为 1。
"""
# python中字符通过ascii相减不像c++可以直接减，可以通过ord()传入一个字符转换成对应
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = maxCost
        window = []
        left = 0
        right = 0
        ans = 0
        while right < len(s):
            if s[right] == t[right]:
                window.append(s[right])
            else:
                mini_cost = abs(ord(s[right])-ord(t[right]))
                window.append(s[right])
                cost -= mini_cost
            right += 1
            while cost < 0:
                cost += abs(ord(s[left])-ord(t[left]))
                window.pop(0)
                left += 1
            ans = max(ans, len(window))
        return ans


s = "abcd"
t = "acde"
maxCost = 0
solu = Solution()
ans = solu.equalSubstring(s, t, maxCost)
print(ans)


