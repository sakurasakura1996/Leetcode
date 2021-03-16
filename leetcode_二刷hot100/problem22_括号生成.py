from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 这道题限制了n的大小，最大为8，可能的意思就是告诉你暴力法也差不多能过哈
        ans = [{}, {"()"}]
        for i in range(2, n+1):
            a = set()
            tmp = ans[i-1]
            for str in tmp:
                for j in range(len(str)+1):
                    temp = str[:j]+"()"+str[j:]
                    if temp not in a:
                        a.add(temp)
            ans.append(a.copy())
        return list(ans[n])



if __name__ == '__main__':
    solu = Solution()
    ans = solu.generateParenthesis(2)
    print(ans)




