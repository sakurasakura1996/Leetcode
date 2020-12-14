"""
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。
示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
注意：本题与主站 138 题相同
"""
class Node:
    def __init__(self,x:int,next=None,random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dic = {None:None}
        cur = head
        ans = Node(head.val)
        tmp = ans
        while cur:
            tmp.next = Node(cur.val)
            tmp = tmp.next
            dic[cur] = tmp
            cur = cur.next
        tmp = ans.next
        cur = head
        while cur:
            tmp.random = dic[cur.random]  # 这样是可以的，但是要注意dic定义时是dic = {None:None}这样key值可以存储Node型
            cur = cur.next
            tmp = tmp.next
        return ans.next

    # 这道题还是搞了很久，题解中列出了很多种解法，这里记录一下
    def copyRandomList_2(self, head:Node) -> Node:
        # 作者提到了python的浅拷贝和深拷贝，浅拷贝只是创建一个指针，指向同一块内存区域，深拷贝是另外创建一个内存单元
        import copy
        return copy.deepcopy(head)

    def copyRandomList_3(self, head:None) -> Node:
        # 图的基本单元是 顶点，顶点之间的关联关系称为 边，我们可以将此链表看成一个图：
        # 看成图的话，那么就有DFS 和 BFS两种解法了
        # DFS
        def dfs(head):
            if not head:return None
            if head in visited:
                return visited[head]
            # 创建新节点
            copy = Node(head.val,None,None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy

        visited = {}
        return dfs(head)






