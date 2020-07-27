"""
146. LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？
示例:
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""
# python自带了OrderedDict，但是在做这道题时不应该直接用库中数据结构，而应该自己写
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.dic = {}
#         self.cap = []  # 这里的时间复杂度并不是O(1)了，应该用双向链表来代替它，而双向链表在插入删除确实是O(1)的时间复杂度，但是在
#                        # 寻找key时时间复杂度又是O(n)了，所以这里实现O(1)复杂度的关键是 哈希表中的value指向存储实际value的位置，相当于
#                        # 哈希表中存储的是引用。这样我们就可以根据哈希表O(1)时间复杂度的办法来查找到key了
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key in self.dic:
#             self.cap.remove(key)
#             self.cap.append(key)
#             return self.dic[key]
#         return -1
#
#     def put(self, key:int, value:int) -> None:
#         if key in self.cap:
#             self.dic[key] = value
#             self.cap.remove(key)
#             self.cap.append(key)
#         elif len(self.cap) < self.capacity:
#             self.dic[key] = value
#             self.cap.append(key)
#         else:
#             remove_key = self.cap[0]
#             self.cap.remove(remove_key)
#             self.dic.pop(remove_key)
#             self.cap.append(key)
#             self.dic[key] = value

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# 先创建一个双线链表结构

class LRUCache:

    def __init__(self, capacity:int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key:int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key:int, value:int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果key存在
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)



