from collections import Counter
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # arr的长度是300，感觉可以直接暴力点啊，不过可以先计算前缀和, 暴力法算是过去了
        preSum = [arr[0]]
        n = len(arr)
        for i in range(1, n):
            preSum.append(preSum[-1] ^ arr[i])

        ans = 0
        for i in range(0, n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    if i == 0:
                        triplet_left = preSum[j-1]
                        triplet_right = preSum[k] ^ preSum[j-1]
                    else:
                        triplet_left = preSum[j-1] ^ preSum[i-1]
                        triplet_right = preSum[k] ^ preSum[j-1]
                    if triplet_left == triplet_right:
                        ans += 1
        return ans

    def countTriplets2(self, arr: List[int]) -> int:
        # 我们没有推理出一个东西，如果 a == b的话，那么 Si = Sk+1了，可以用两重循环就能写出来
        # 而且，当等式 Si = Sk+1成立时，[i+1, k]的范围内的任意j都是符合要求的，对应的三元组个数为 k-i。因此我们只需要枚举 i和k就行了
        n = len(arr)
        preSum = [0]
        for val in arr:
            preSum.append(preSum[-1] ^ val)

        ans = 0
        for i in range(n):
            for k in range(i+1, n):
                if preSum[i] == preSum[k+1]:
                    ans += k - i
        return ans

    def countTriplets3(self, arr: List[int]) -> int:
        # 竟然还可以用一重循环,用哈希表
        # 这个方法就需要数学比较好了，可以稍微推导一下, 对于下标k，若下标 i = i1, i2,...im时均满足 Si = Sk+1,那么根据方法二，这些二元组
        # (i1, k),(i2, k)...(im,k)对答案的贡献之和为：
        #    (k-i1) + (k-i2) +...+ (k-im) = m * k - (i1 + i2 +...im),也就是说遍历下标k，我们需要知道所有满足 Si = Sk+1的
        # 下标i的出现次数m，下标i之和，这可以借助两个哈希表来做到。在遍历下标k的同时，一个哈希表统计Sk的出现次数，另一个哈希表统计值为Sk的下标之和
        n = len(arr)
        preSum = [0]
        for val in arr:
            preSum.append(preSum[-1] ^ val)
        cnt, total = Counter(), Counter()
        ans = 0
        for k in range(n):
            if preSum[k+1] in cnt:
                ans += cnt[preSum[k+1]] * k - total[preSum[k+1]]
            cnt[preSum[k]] += 1
            total[preSum[k]] += k
        return ans




if __name__ == '__main__':
    solu = Solution()
    arr = [1,1,1,1,1]
    ans = solu.countTriplets(arr)
    print(ans)