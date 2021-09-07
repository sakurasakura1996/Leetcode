from collections import Counter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 使用简单的方法来写，需要用额外的空间复杂度，
        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value == 1:
                return key

    def singleNumber2(self, nums: List[int]) -> int:
        # 我总是不太会写常数空间复杂度的方法啊。。。只是知道大概率是用位运算，异或，and or这种运算来写。可是具体怎么写，搞不定。
        # 使用位运算 可以实现 O(1)的空间复杂度
        #  ~x      表示  位运算 Not    非
        #  x & y   表示  位运算 AND    与
        #  x + y   表示  位运算 XOR    异或
        # XOR 该运算符用于检测出现奇数次的位：1、3、5等
        # 0 与任何数XOR结果为该数。    0 XOR x = x
        # 两个相同的数XOR结果为0.     x XOR  x = 0
        # 以此类推，只有某个位置的数值出现奇数次时，该位的掩码才不为0. 因此可以检测出出现一次的位和出现三此的位，但是要注意区分这两种情况
        #　AND 和 NOT  为了区分出现一次的数字和出现三次的数字，使用两个掩码：seen_once 和 seen_twice
        # 思路是 仅当 seen_twice 未变时，改变seen_once. 仅当 seen_once未变时，改变seen_twice
        # 位掩码 seen_once仅保留出现一次的数字，不保留出现三次的数字。
        seen_once = seen_twice = 0

        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            print(seen_once)
            seen_twice = ~seen_once & (seen_twice ^ num)
            print(seen_twice)

        return seen_once


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 2, 3, 2]
    ans = solu.singleNumber2(nums)
    print(ans)