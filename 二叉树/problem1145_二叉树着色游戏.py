"""
1145. 二叉树着色游戏
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。
游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，
「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；
「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。
「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。
之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。
如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。
若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。
现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。
输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：True
解释：第二个玩家可以选择值为 2 的节点。
提示：
二叉树的根节点为 root，树上由 n 个节点，节点上的值从 1 到 n 各不相同。
n 为奇数。
1 <= x <= n <= 100
"""
# 我们来分析一下：
# 1.如果第一个玩家他选了根节点：
#   如果左右子树个数不一样，那我选那颗节点数多的子树根节点，那么我就赢了
#   如果左右子树个数一样，那我稳输了呀宝贝
# 2.如果第一个玩家他选择的是根节点左右子树中其中一颗子树的节点。
#   如果他选的是那颗节点数少的子树中的一点或者两颗子树节点数相同，那我肯定赢了，我选根节点就行了
#   如果他选的是那颗节点数多的子树中的一点，那我还是有可能赢，就是他选的比较靠底层的节点。 么怎么判断呢？有点像下棋一样
#       我们计算一下以他选的节点为根的树总共有多少节点，如果小于一半，那我就赢了，OK，先这样写
#       发现我思考的角度还是有漏洞，就是如果第一个玩家选了一个子树较多的节点，且比较靠近高层，但是他的子树几乎是其余所有节点，
#       这个时候，我们判断它的总节点数大于一半，但是第二个玩家并不一定会输啊。
# 所以应该这样说，如果可以找到一颗子树，节点数大于一半，那么我们就可以赢啊，但是这颗子树内没有第一个玩家选的节点。


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numOfSubNode(self, node:TreeNode)->int:
        # 返回以该节点为根节点的子树节点个数
        if not node:
            return 0
        ans = 1
        if node.left:
            ans += self.numOfSubNode(node.left)
        if node.right:
            ans += self.numOfSubNode(node.right)
        return ans

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if n == 1:
            return False
        if x == root.val:
            if self.numOfSubNode(root.left) == self.numOfSubNode(root.right):
                # 如果左右子树节点数相同，而第一个玩家选的是根节点，那我就输了
                return False
            else:
                return True
        else:
            # 需要找到他选的那个节点，我们需要遍历二叉树找到他，然后计算该节点为根节点的子树有多少个节点。
            from collections import deque
            stack = deque()
            stack.append(root)
            while stack:
                node = stack.popleft()
                if node.val == x:
                    ans = self.numOfSubNode(node)
                    if ans <= n//2:
                        return True
                    elif self.numOfSubNode(node.left) >= n//2 or self.numOfSubNode(node.right) >= n//2:
                        return True
                    else:
                        return False

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)




