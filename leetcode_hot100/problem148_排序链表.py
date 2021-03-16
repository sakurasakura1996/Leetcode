"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
进阶：
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]
提示：
链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 简单的方法就是遍历一遍，然后排个序，再遍历一遍将值给改掉，但是空间复杂度不符合进阶要求
        if not head:
            return head
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.nexat
        nums.sort()
        cur = head
        for i in range(len(nums)):
            cur.val = nums[i]
            cur = cur.next
        return head


    def sortList2(self, head: ListNode) -> ListNode:
        # 我们再来看看，怎么实现常数级空间复杂度呢，首先，如果没有想法，我们是不是可以联想这类题目可能有什么点子呢，比如 双指针对吧。
        # 或者题目既然是排序，那么我们就应该要联想到有哪些排序算法吧，虽然平常都是根据数组来排序，但是链表排序思路应该也一样啊。
        # 前面已经实现了一遍链表的插入排序过程，时间复杂度是平方级别的，不符合题意，那么我们想想看还有什么 nlogn的方法是符合题意的

        # 这里先实习一下自顶向下的归并排序
        def merge(node1: ListNode, node2: ListNode):
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, node1, node2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next






