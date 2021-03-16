
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        ans = ""
        while word1 and word2:
            if word1 >= word2:
                ans += word1[p1]
                word1 = word1[1:]
            else:
                ans += word2[p2]
                word2 = word2[1:]
        if word1:
            ans += word1
        if word2:
            ans += word2
        return ans


if __name__ == '__main__':
    solu = Solution()
    word1 = "abcabc"
    word2 = "abdcaba"
    ans = solu.largestMerge(word1, word2)
    print(ans)