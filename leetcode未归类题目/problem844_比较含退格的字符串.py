"""
844. 比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

示例 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。

示例 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

示例 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

提示：
1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
进阶：
你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        s = list(S)
        t = list(T)
        for s_item in s:
            if s_item != '#':
                s_stack.append(s_item)
            elif s_stack:
                s_stack.pop(-1)

        for t_item in t:
            if t_item != '#':
                t_stack.append(t_item)
            elif t_stack:
                t_stack.pop(-1)
        # 再比较两个栈是否内容相同
        if len(s_stack) == len(t_stack) and all(map(lambda x, y: x == y, s_stack, t_stack)):
            return True
        else:
            return False

    # 题解提供了O(N)时间复杂度，O(1)空间复杂度的方法，双指针方法。此方法利用倒序遍历
    def backspaceCompare2(self, S: str, T: str) -> bool:
        i, j = len(S)-1, len(T)-1
        delNumberS = delNumberT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    delNumberS += 1
                    i -= 1
                elif delNumberS > 0:
                    delNumberS -= 1
                    i -= 1
                else:
                    # 当前所指的字符是会留下的字符，那就去和T中留下的字符对比
                    break
            while j >= 0:
                if T[j] == '#':
                    delNumberT += 1
                    j -= 1
                elif delNumberT > 0:
                    delNumberT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True

solu = Solution()
S = "a##c"
T = "#a#c"
ans = solu.backspaceCompare2(S, T)
print(ans)