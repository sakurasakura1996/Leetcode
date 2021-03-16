"""
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
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
from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        cur_idx = 0
        for i in range(len(postorder)):
            if postorder[i] >= root:   # 这里的等于号十分关键啊。。。如果没有右节点，那就默认为0了。
                cur_idx = i
                break
        left = postorder[:cur_idx]
        right = postorder[cur_idx:-1]
        for val in right:
            if val < root:
                return False
        return self.verifyPostorder(left) and self.verifyPostorder(right)


if __name__ == '__main__':
    solu = Solution()
    postorder = [4, 6, 7, 5]
    ans = solu.verifyPostorder(postorder)
    print(ans)