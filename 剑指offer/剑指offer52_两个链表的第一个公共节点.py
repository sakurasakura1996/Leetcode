"""
剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。
如下面的两个链表：
在节点 c1 开始相交。
示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
本题与主站 160 题相同
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n)时间复杂度，O(1)空间复杂度的方法暂时想不出来
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = []
        B = []
        pa = headA
        pb = headB
        while pa:
            A.append(pa)
            pa = pa.next
        while pb:
            B.append(pb)
            pb = pb.next
        la = len(A)-1
        lb = len(B)-1
        while la >= 0 and lb >= 0 and A[la] == B[lb]:
            la -= 1
            lb -= 1
        if la < 0:
            return headA
        if lb < 0:
            return headB
        for i in range(la):
            headA = headA.next
        return headA.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 这个方法怎么说呢，是属于那种智力题，想不到就是想不到我感觉
        # 假设两者的公共部分长度为C，headA独立部分长度为L1，headB独立长度为L2，那最后两者相遇都是走了L1+L2+C
        nodea, nodeb = headA, headB
        while nodea != nodeb:
            nodea = nodea.next if nodea else headB
            nodeb = nodeb.next if nodeb else headA
        return nodea

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 我为啥这么蠢呢，这道题感觉下面这个想法我应该很快就能写出来啊，可是最后我竟然没有想出来。。。。
        # 计算两个链表的长度，然后长一点的先走两者差值的步数，最后两个人再一起走，遇到了就返回结果。
        node1, node2 = headA, headB
        len1 = 0
        len2 = 0
        while node1:
            len1 += 1
            node1 = node1.next
        while node2:
            len2 += 1
            node2 = node2.next
        if len1 > len2:
            for i in range(len1 - len2):
                headA = headA.next
        if len2 > len1:
            for i in range(len2 - len1):
                headB = headB.next
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA










