"""
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，
把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
返回转换后的单向链表的头节点。
注意：本题相对原题稍作改动
示例：
输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：
节点数量不会超过 100000。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binode-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = TreeNode(1)
    head = ans
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        # 二叉搜索树的特性就是中序遍历返回的结果就是有序的，那么我们在中序遍历过程中生成这个链表
        # 先试试用递归的中序遍历能不能解决
        if not root:
            return
        # if root.left:  这里不应该加判断条件，因为题目答案实例中有null。
        self.convertBiNode(root.left)
        # 访问根节点
        self.head.left = None
        self.head.right = root
        self.head = root
        self.convertBiNode(root.right)
        return self.ans.right
        # 提交上面代码结果超时。

    def convertBiNode_2(self, root: TreeNode)-> TreeNode:
        # 下面的递归方法超时了，但是也很慢了，看来递归方法不是很好
        if root is None: return None
        left_head = self.convertBiNode(root.left)
        right_head = self.convertBiNode(root.right)
        root.left = None
        root.right = right_head
        head = root
        if left_head:
            head = left_head
            while left_head.right:
                left_head = left_head.right
            left_head.right = root
        return head

    def convertBiNode_3(self, root: TreeNode) -> TreeNode:
        # 使用非递归方法来写写,那就是中序遍历的非递归方法了，需要使用栈
        # woca,怎么自己写的方法总是超时啊。感觉非递归也就只能这样写了啊。
        stack = []
        ans = TreeNode(-1)
        tmp = ans
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                node.left = None  # 找到超时的地方了，我原来这里写的是 tmp.left = None
                # 但是我没有搞懂，tmp.right = None 为什么会直接让程序运行超时呢，
                # 去除这句的话测试竟然也会超时，这是什么鬼，难道和答案中的那个null有关吗
                tmp.right = node
                tmp = node
                root = node.right
        return ans.right

    def convertBiNode_4(self, root: TreeNode) -> TreeNode:
        # 这是别人写的非递归方法，竟然接近双百了，这特么怎么回事啊
        start = prev = TreeNode(-1)
        stack = []
        node = root
        while node is not None or stack:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node.left = None
                prev.right = node
                prev = node
                node = node.right
        return start.right


