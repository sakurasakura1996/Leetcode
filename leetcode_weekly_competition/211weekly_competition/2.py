class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        def canculate(string):
            ans = '9' * n
            # 计算这个字符串，不断加a过程中最小的字符串
            s = list(string)
            for i in range(10):
                for j in range(1, n, 2):
                    s[j] = str(int(s[j])+a) if int(s[j])+a < 10 else str(int(s[j])+a-10)
                if int(''.join(s)) < int(ans):
                    ans = ''.join(s)
            return ans

        def canculate2(string):
            ans = '9' * n
            # 计算这个字符串，不断加a过程中最小的字符串
            s = list(string)
            for i in range(10):
                for j in range(0, n, 2):
                    s[j] = str(int(s[j])+a) if int(s[j])+a < 10 else str(int(s[j])+a-10)
                if int(''.join(s)) < int(ans):
                    ans = ''.join(s)
            return ans

        if b%2 == 1:
            # b为奇数的话，所有位都能加a，
            candidate = []
            for i in range(n):
                candidate.append(s[i:]+s[:i])
            ans = '9' * n
            for can in candidate:
                item = canculate(can)
                item2 = canculate2(can)
                if int(item) < int(ans):
                    ans = item
                if int(item2) < int(ans):
                    ans = item2

            return ans
        else:
            # b为偶数的话，只有奇数位能加到a，但是只有偶数位能作为开头。所以找到偶数位中最小的那个。
            min_start = 9
            min_idx = []
            candidate = []
            for i in range(0, n, 2):
                if int(s[i]) < min_start:
                    min_start = int(s[i])
            for i in range(0, n, 2):
                if int(s[i]) == min_start:
                    min_idx.append(i)
                    candidate.append(s[i:]+s[:i])
            # 找到了候选项，然后计算这些候选项中哪个最小。
            ans = int('9'* n)
            for can in candidate:
                item = canculate(can)
                if int(item) < int(ans):
                    ans = item
            return ans

    def findLexSmallestString2(self, s: str, a: int, b: int) -> str:
        b = b%len(s)

        def addOperation(s):
            ans = list(s)
            for i in range(1, len(s), 2):
                ans[i] = str((int(s[i])+a))[-1]
            return ''.join(ans)

        def lunOperation(s):
            return s[-b:]+s[:-b]
        alls = {s}

        def dfs(s):
            alls.add(s)
            print(alls)
            s1 = addOperation(s)
            s2 = lunOperation(s)
            if s1 not in alls:
                dfs(s1)
            if s2 not in alls:
                dfs(s2)
        dfs(s)
        return min(alls)


solu = Solution()
s = "74"
a = 5
b = 1
ans = solu.findLexSmallestString2(s, a, b)
print(ans)