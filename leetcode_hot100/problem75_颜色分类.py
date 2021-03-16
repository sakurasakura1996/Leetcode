"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

示例 3：
输入：nums = [0]
输出：[0]

示例 4：
输入：nums = [1]
输出：[1]
提示：
n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
进阶：
你可以不使用代码库中的排序函数来解决这道题吗？
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""
# 没太懂为什么这道题是一个中等难度，我直接遍历一遍，然后记录一下0，1，2的个数，最后再直接赋值不行吗
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = [0, 0, 0]
        n = len(nums)
        for i in range(n):
            counter[nums[i]] += 1
        nums[:counter[0]] = [0] * counter[0]
        nums[counter[0]:counter[0]+counter[1]] = [1] * counter[1]
        nums[counter[0]+counter[1]:] = [2] * counter[2]

    def sortColors2(self, nums: List[int]) -> None:
        # 题解中的单指针方法
        p = 0
        n = len(nums)
        for i in range(p, n):
            if nums[i] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        for i in range(p, n):
            if nums[i] == 1:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1



"""
题解中提到，这道题是经典的  【荷兰国旗问题】，是 大名鼎鼎的 Dijkstra 首先提出，下面阐述题解中的多种方法
方法一：就是我们上面写的方法，这很容易想到
方法二：基于指针进行交换的方法——>单指针：
    这个方法的意思就是，我们两次遍历数组，第一次把所有的0排到数组的前面，第二次遍历把所有的1排到后面，那么剩下的2就都在数组最后面了
方法三：题解中的意思是，方法二需要两次遍历，那么我们是否可以只用遍历一次呢，可以，就是再加一个指针就可以了。

    
"""

if __name__ == '__main__':
    solu = Solution()
    nums = [1]
    solu.sortColors(nums)
    print(nums)

