class Solution:
    """
    @param num: array of num
    @param ask: Interval pairs
    @return: return the sum of xor
    """
    def Intervalxor(self, num, ask):
        # write your code here
        l1, r1, l2, r2 = ask[0][0], ask[0][1], ask[0][2], ask[0][3]
        ans = max(num[l1-1:r1]) + min(num[l2-1:r2])
        n = len(ask)
        for i in range(1,n):
            ask_item = ask[i]
            l1, r1, l2, r2 = ask_item[0], ask_item[1], ask_item[2], ask_item[3]
            cur = max(num[l1-1:r1]) + min(num[l2-1:r2])
            ans = ans ^ cur
        return ans


solu = Solution()
num = [1,2,3,4,5]
ask = [[1,2,3,4],[1,2,4,5]]
ans = solu.Intervalxor(num, ask)
print(ans)