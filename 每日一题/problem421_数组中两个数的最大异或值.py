from typing import List
class Trie:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 字典树的根节点
        root = Trie()
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        def add(num: int):
            # 将num转换为二进制串然后放入到字典树或者说前缀树当中。
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def check(num: int) -> int:
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    # a_i 的第k个二进制位为0，应当往表示1的子节点right走
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    # a_i 的第k个二进制位为1，应当往表示0的子节点left走
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x

        n = len(nums)
        x = 0
        for i in range(1, n):
            # 将nums[i-1]放入字典树，此时nums[0..i-1]都在字典树中
            add(nums[i-1])
            # 将nums[i]看作ai，找出最大的x更新答案
            x = max(x, check(nums[i]))
        return x


if __name__ == '__main__':
    solu = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    ans = solu.findMaximumXOR(nums)
    print(ans)


