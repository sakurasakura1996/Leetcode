class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 思考简单点的话，我们直接拿list()来存储下节点，然后改下就行，这个思路简单，但是空间复杂度变成O（n)
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        while left < right:
            nodes[left-1], nodes[right-1] = nodes[right-1], nodes[left-1]
            left += 1
            right -= 1
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[len(nodes)-1].next = None
        return nodes[0]

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        # 我们先想好把要反转的链表拆下来，然后调用子函数，然后再拼接起来就行了。
        def reverse_linked_list(head: ListNode):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        # 第一步：从虚拟节点走 left - 1步，来到left节点的前一个节点
        # 建议写在for循环里，语义清晰
        for _ in range(left - 1):
            pre = pre.next

        # 第二步：从pre再走right-left+1步，来到right节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next

        # 第三步：切断出一个子链表
        left_node = pre.next
        curr = right_node.next

        # 注意切断链表
        pre.next = None
        right_node.next = None

        reverse_linked_list(left_node)

        pre.next = right_node
        left_node.next = curr
        return dummy.next



if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    ans = solu.reverseBetween2(head, 1, 2)
    while ans:
        print(ans.val)
        ans = ans.next

