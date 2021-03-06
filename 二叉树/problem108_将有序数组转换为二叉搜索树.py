"""
108.将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 记得以前考研的时候遇到过这种问题，平衡二叉树的构建构成，和堆的构建有点混杂了
# 当然我们也可以这样做，构建的是二叉搜索树，那么我们每次平分数组，中间的数做根节点。
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        nums_len = len(nums)
        mid = int(nums_len/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:nums_len])
        return root
    # 不得不说，树问题递归方法还是思路顺畅啊
    

