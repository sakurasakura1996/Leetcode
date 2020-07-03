"""
1028.从先序遍历还原二叉树
我们从二叉树的根节点 root 开始进行深度优先搜索。
在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
如果节点只有一个子节点，那么保证该子节点为左子节点。
给出遍历输出 S，还原树并返回其根节点 root。
实例：
输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
提示：
原始树中的节点数介于 1 和 1000 之间。
每个节点的值介于 1 和 10 ^ 9 之间。
"""
# 二叉树先序遍历的实质是DFS，那么这题就有一个很重要的性质存在，通过S访问到的节点，其父节点肯定是访问过上一层的节点中的最后一个啦
# 这题感觉不难，就是这个先序遍历使用一个S字符串来给你的，还要处理下这个字符串。就很蛋疼
# 结合使用 字典应该ok，根据数字前的-数量来计算它所在的层数。

# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        level = 0    # 节点层数
        num = 0    # 记录节点的值的
        n = len(S)
        dic = defaultdict(list)
        for i, c in enumerate(S):
            if c == '-':
                level += 1
            else:
                num = num * 10 + int(c)
                if i == n - 1 or S[i+1] == '-':
                    # num值就是一个TreeNode.val，它的父节点就是 dic上一层中的最后一个节点
                    node = TreeNode(num)
                    dic[level].append(node)
                    if dic[level-1]:
                        if dic[level-1][-1].left:
                            dic[level-1][-1].right = node
                        else:
                            dic[level-1][-1].left = node
                    num = 0
                    level = 0
                    # 该节点已经创建了，那么下一个节点的val值和所属层次level都要重新计算的
        return dic[0][0]


