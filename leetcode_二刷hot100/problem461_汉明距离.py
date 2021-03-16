class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        print(type(bin(x ^ y)))
        return bin(x ^ y).count('1')

    def hammingDistance2(self, x: int, y: int) -> int:
        # 除了使用上面的 count内置函数，为了计算1的个数，可以将每个位移动到最左端或最右端，然后检查
        # 该位是否为1，更准确的说，应该进行逻辑移位，移入零替换丢弃的位。这里采用右移位，每个位置都会被移动到最右边。
        # 移位后检查最右位的位是否为 1 即可。检查最右位是否为 1，可以使用取模运算（i % 2）或者 AND 操作（i & 1），
        # 这两个操作都会屏蔽最右位以外的其他位。
        xor = x ^ y
        ans = 0
        while xor:
            if xor % 2:
                ans += 1
            xor = xor >> 1
        return ans




if __name__ == '__main__':
    solu = Solution()
    x = 1
    y = 4
    ans = solu.hammingDistance2(x, y)
    print(ans)