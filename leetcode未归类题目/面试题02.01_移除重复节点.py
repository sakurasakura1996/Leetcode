"""
面试题 02.01. 移除重复节点
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]

示例2:
 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
提示：
链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。
进阶：
如果不得使用临时缓冲区，该怎么解决？
"""


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


# 使用缓存区的话就很简单啦，用一个哈希表来记录是否出现
class Solution:
    def removeDuplicateNodes(self, head:ListNode) -> ListNode:
        dic = {}
        ans = head
        prev = head
        while head:
            if head.val not in dic:
                dic[head.val] = 1
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = prev.next
        return ans

    def removeDuplicateNodes_2(self, head:ListNode) -> ListNode:
        # 如果想不额外添加缓存，而又达到上述方法的O(N)时间复杂度是不可能的，所以只能增加时间复杂度到O(N^2),采用两重循环
        # python语言用此种方法不能通过提交，晕了
        ans = head
        while head:
            target = head.val
            Node = head
            while Node.next:
                if Node.next.val == target:
                    Node.next = Node.next.next
                else:
                    Node = Node.next
            head = head.next
        return ans


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(3)
a5 = ListNode(2)
a6 = ListNode(1)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
solu = Solution()
ans = solu.removeDuplicateNodes_2(a1)
while ans:
    print(ans.val)
    ans = ans.next