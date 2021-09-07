from typing import List
from functools import reduce
from operator import xor
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True

        xorsum = reduce(xor, nums)
        return xorsum == 0

        # 我们可以思考一下。算了，看了题解之后，我觉得我目前不需要钻研这类体型，性价比太小
