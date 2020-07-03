"""
通常前序遍历，中序遍历，后序遍历这三者，只要有一个中序遍历加上其他任意一个都是可以还原二叉树的
正好我们来熟悉这个过程的代码实现。由前序遍历和中序遍历输出后序遍历，由后序遍历和中序遍历输出前序遍历
同时还有一个层次遍历，层次遍历加上某一个遍历也可以还原这棵二叉树，我们都全部实现一遍吧
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PreAndIn2Tree:
    """
    该方法用于给定先序遍历和中序遍历还原二叉树
    思路记录：先序遍历，第一个元素肯定是根节点，然后中序遍历该节点值的左边都是根节点的左子树部分，右边部分都是根节点的右子树部分。
    那我们可以用递归来实现吗？可以第一个方法就是递归方法，那么如何不用递归方法呢？第二种方法采用迭代方法来实现：
    我们用一个栈stack来维护 当前节点的所有还没有考虑过右儿子的祖先节点，栈顶就是当前节点。也就是说，只有在栈中的节点才可能连接一个新的
    右儿子。同时，我们用一个指针index指向中序遍历的某个位置，初始值为0。index对应的节点是 当前节点不断往左走到达的最终节点， 这也是
    符合中序遍历的，它的作用在下面的过程中会有所体现。
    """
    def preIn2Post(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归方法
        # 首先一定要注意初始化和特殊值情况。
        if not preorder:
            return None
        tree_len = len(preorder)
        if tree_len == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        # 接下来如果想递归的话，中序遍历的数组还比较好分开，前序遍历的数组就要分出根节点的左右子树部分来，另外假设树是没有重复元素的
        root_idx = inorder.index(root.val)
        root.left = self.preIn2Post(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.preIn2Post(preorder[root_idx+1:], inorder[root_idx+1:])
        # 注意这里的数组取值如果冒号后面写-1的话最后一个值没有取到，直接省略就可以了
        return root

    def preIn2Post_2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 非递归方法 ->迭代方法
        # 对于前序遍历中的任意两个连续节点u和v，根据前序遍历的流程，我们可以知道u和v只有两种可能的关系：
        # 1.v是u的左儿子，  2.u没有左儿子，并且v是u的某个祖先节点（或者u本身）的右儿子，如果u没有左儿子，那么下一个遍历的节点就是u
        # 的右儿子。如果u没有右儿子，我们就会向上回溯，直到遇到第一个有右儿子（且u不在它的右儿子的子树中）的节点ua，那么v就是ua的右儿子
        # 具体过程想要说清楚还是挺复杂的。
        # https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root


class PostAndIn2Tree:
    """
    该类方法用于给定后序遍历和中序遍历还原二叉树,递归方法的关键在于想明白，后序和中序的顺序和逻辑。
    同时，这里写的递归方法是直接就原函数进行递归的，那么递归函数对两个数组进行了切片，如果另外定义递归函数的话
    可以将参数改成 索引位置值，这样不会切片数组，提高时间和空间复杂度。
    中序和后序遍历还原二叉树的方法 好像没有上面的迭代法，后面如果遇到了可以来这里进行补充
    """
    def postIn2Pre(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 递归方法求解。需要利用的点就是后序遍历最后一个值就是整棵树的根节点
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(root.val)
        root.left = self.postIn2Pre(inorder[:root_idx], postorder[:root_idx])
        root.right = self.postIn2Pre(inorder[root_idx+1:], postorder[root_idx:-1])
        return root


class PreAndPost2Tree:
    """
    该类方法用于返回与给定的前序遍历和后序遍历匹配的任何二叉树。
    因为，从原理上来说，给定前序和后序遍历是不能唯一确定一棵二叉树的。所以题目改成了输出其中成立的一个就可以了。
    注意：这里写的方法在空间复杂度上也是不够优的，可以使用数组的索引作为函数的参数，这样就避免了每次调用自身的时候都要重新创建数组切片部分。
    """

    def prePost2Tree(self, preorder:List[int], postorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        if preorder[1]!=postorder[-2]:
            # 这个条件下，左右子树都有
            right_index = preorder.index(postorder[-2])

            root.left = self.prePost2Tree(preorder[1:right_index], postorder[:right_index-1])
            root.right = self.prePost2Tree(preorder[right_index:], postorder[right_index-1:-1])
        else:
            # root节点下只有一个子节点，左右子节点都符合题意
            root.left = self.prePost2Tree(preorder[1:],postorder[:-1])
        return root

    def prePost2Tree_2(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        # 正如解析中提到的，上面的方法空间复杂度不是很好，因为对数组进行了切分，浪费了时间和空间复杂度，这里用索引来作为函数参数进行编码
        def make(i0, i1, N):   # 这里的 i0 i1 N 指的是 preorder[i0:i0+N],postorder[i1:i1+N]
            if N == 0:return None
            root = TreeNode(preorder[i0])
            if N == 1:return root

            for L in range(N):
                if postorder[i1 + L -1] == preorder[i0 + 1]:
                    break
            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root
        return make(0, 0, len(preorder))

