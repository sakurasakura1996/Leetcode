"""
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false
示例 2：
输入: [1,3,2,6,5]
输出: true
提示：
数组长度 <= 1000
"""
# 检查是否是二叉搜索树的后序遍历结果，那么我们就根据其后序遍历结果还原二叉树。由于需要中序加后序才能恢复出这棵二叉树
# 那么中序遍历好搞啊，假设他就是二叉搜索树，那么中序遍历有序，也就是数组排个序就是了。
# 但是这里并不是要还原二叉树，而是判断一个序列是不是二叉搜索树的后序遍历序列，只用判断大小关系
from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m-1) and recur(m, j-1)

        return recur(0, len(postorder) - 1)

    def verifyPostorder2(self, postorder: List[int]) -> bool:
        if not postorder: return True
        root = postorder[-1]
        cur_index = 0
        for i in range(len(postorder)):
            if postorder[i] >= root:
                cur_index = i
                break
        left = postorder[:cur_index]
        right = postorder[cur_index : -1]
        for val in right:
            if val < root:
                return False
        return self.verifyPostorder(left) and self.verifyPostorder(right)




if __name__ == '__main__':
    postorder = [1,3,2,6,5]
    solu = Solution()
    ans = solu.verifyPostorder(postorder)
    print(ans)







