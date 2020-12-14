class Solution:
    """
    @param s: a string.
    @return: return the values of all the intervals.
    """
    def suffixQuery(self, s):
        # write your code here
        from collections import defaultdict
        n = len(s)
        dic = defaultdict(list)
        # 把相同字符的索引放在一块
        for i in range(n):
            dic[s[i]].append(i)

        def search(s, i, j):
            left = i
            right = j
            number = 0
            while left < right:
                if s[left] == s[right]:
                    number += 1
                    left += 1
                    right -= 1
                else:
                    break
            return number

        def solve(s, v):
            if not v or len(v) == 1:
                return 0
            n = len(v)
            num = 0
            for i in range(n-1):
                for j in range(i+1,n):
                   num += search(s, v[i], v[j])
            return num

        ans = 0
        for k, v in dic.items():
            ans += solve(s, v)
        return ans + n


solu = Solution()
s = "bacbdadb"
ans = solu.suffixQuery(s)
print(ans)
