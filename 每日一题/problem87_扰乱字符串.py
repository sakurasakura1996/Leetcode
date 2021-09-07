from collections import Counter
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def isScramble(self,s1: str, s2: str) -> bool:
        # 我这属于暴力法，提交之后超出时间限制了。。。最后采用记忆化递归可以解决该问题。题解中给的是动态规划方法，但其实，这类问题，如果可以用
        # 动态规划来解决，那么很大程度上，我们也可以用记忆化递归来求解。
        if len(s1) == 1:
            return s1 == s2
        if Counter(s1) != Counter(s2):
            return False
        flag = False
        for i in range(1, len(s1)):
            s1_left = Counter(s1[:i])
            s1_right = Counter(s1[i:])
            s2_left = Counter(s2[:i])
            s2_right = Counter(s2[-i:])
            if s1_left == s2_left:
                flag = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
                if flag:
                    return True
            if s1_left == s2_right:
                flag = self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
                if flag:
                    return True
        return flag

    # def isScramble2(self, s1: str, s2: str) -> bool:
        # 还有没有其他方法啊。


if __name__ == '__main__':
    solu = Solution()
    s1 = "eebaacbcbcadaaedceaaacadccd"
    s2 = "eadcaacabaddaceacbceaabeccd"
    ans = solu.isScramble(s1, s2)
    print(ans)


