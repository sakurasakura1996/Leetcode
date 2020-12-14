"""
1379. 找出克隆二叉树中的相同节点
给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。
其中，克隆树 cloned 是原始树 original 的一个 副本 。
请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。

注意：
你 不能 对两棵二叉树，以及 target 节点进行更改。
只能 返回对克隆树 cloned 中已有的节点的引用。
进阶：如果树中允许出现值相同的节点，你将如何解答？

提示：
树中节点的数量范围为 [1, 10^4] 。
同一棵树中，没有值相同的节点。
target 节点是树 original 中的一个节点，并且不会是 null 。
示例1
输入: tree = [7,4,3,null,null,6,19], target = 3
输出: 3
解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 那我就对第一棵树进行遍历呗，同时对克隆的树也进行遍历，然后如果找到了这个节点，直接返回克隆树上的节点引用

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return original
        if original == target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)

        right = self.getTargetCopy(original.right,cloned.right,target)
        if left:
            return left
        if right:
            return right
