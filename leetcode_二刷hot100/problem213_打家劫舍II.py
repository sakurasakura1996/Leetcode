from typing import List
class Solution:
    # II相比I，在原来的基础上添加了环形的条件，也就是如果偷了第一家，最后一家是不能偷了。
    # 我们定义dp数组可以用不同的含义，比如dp[i]表示偷前i家，所得的最大收入，或者说偷前i家，且要偷第i家。
    # 这道题目我竟然想不出来咋整，或者说是麻烦的思路我都不想写了，看了题解之后才有了思路，这里的主要问题主要还是环，那么
    # 那么也就是考虑第一个和最后一个不能同时偷的问题，如果偷第一个，那就是nums[:-1]嘛，如果不偷第一个的话，那就是nums[1:]，然后
    # 再在打家劫舍I的基础上来解决问题。
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            # 接下来的写法，可谓大佬写法。。。
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre+num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]








