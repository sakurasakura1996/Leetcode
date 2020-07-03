"""
23.合并k个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
# 当然最笨的方法还是把所有的链表节点值放入到列表中，然后排序，最后生成链表返回就行了
# 但是这个方法就很蠢的感觉，时间复杂度为 O(NlogN) N是lists数组元素的个数。

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists_1(self, lists: List[ListNode]) -> ListNode:
        # 暴力法，所有的值拿出来在排个序，最后生成一个链表返回头节点就可以了
        # if not lists: 这种判断只能判断lists不为空，
        if not lists or len(lists) == 0:
            return None
        ans = []
        for list_node in lists:
            while list_node:
                ans.append(list_node.val)
                list_node = list_node.next
        ans.sort()
        # head = ListNode(ans[0]) 这样写报错数组越界，那么上面的判断数组不为空还不够吗，报错输入案例是 [[]]那么这个案例满足了上面的判断吗
        head = ListNode(None)
        ans_node = head
        for i in range(len(ans)):
            head.next = ListNode(ans[i])
            head = head.next
        return ans_node.next
    # wca,就这暴力法还能在python中击败88%的人，有时候怀疑这个力扣判断是不是有问题

    def mergeLists_2(self, lists: List[ListNode]) -> ListNode:
        # 使用优先队列（堆）来实现
        if not lists or len(lists) == 0:
            return None
        import heapq
        # 这个包还没用过，熟悉熟悉
        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出（因为是小顶堆，所以每次出来的都是目前堆中值最小的元素）然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heapq.heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next
    # 上面的代码，主要还是了解了解这个heapq的使用，应该是相关于堆的包。堆其实就是用一个数组来表示一颗二叉树，
    # 大堆的特点就是父节点比子节点的值都大，小堆的特点就是父节点比子节点的值都小，那其实这个代码看了下，和暴力法差不多，但是用了堆，排序过程
    # 可能简单很多
    def merge(self, node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:  # 对两个节点的val进行判断，直到一方的next为空
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        # 有一方的next的为空，就没有比较的必要了，直接把不为空的一边加入到结果的next上
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next =cursor_b
        return dummy.next

    def mergeLists_3(self, lists: List[ListNode]) -> ListNode:
        # 分治法
        length = len(lists)
        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return self.merge(self.mergeLists_3(lists[:mid]), self.mergeLists_3(lists[mid:length]))







