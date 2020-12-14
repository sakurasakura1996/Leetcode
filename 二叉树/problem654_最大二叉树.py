"""
654. 最大二叉树
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。
示例 ：
输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：
      6
    /   \
   3     5
    \    /
     2  0
       \
        1
提示：
给定的数组的大小在 [1, 1000] 之间。
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def constructTree(nums:List[int], left:int, right:int):
            if left > right:
                return None
            maxnum = max(nums[left:right+1])
            maxidx = nums.index(maxnum)
            root = TreeNode(maxnum)
            root.left = constructTree(nums,left,maxidx-1)
            root.right = constructTree(nums,maxidx+1,right)
            return root

        root = constructTree(nums,0,len(nums)-1)
        return root