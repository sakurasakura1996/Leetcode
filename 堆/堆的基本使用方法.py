import heapq
# 使用方法1：heapify()将一个列表直接变成一个按照堆进行排序的堆（本质上还是列表）
arr = [3, 45, 6, 4, 0, 54]
heapq.heapify(arr)
print(arr)
# heapq默认是小顶堆，即堆顶是最小元素，如果想用大顶堆，只需把所有入堆的元素都置负即可
# 同时打印上方的arr，可以确定的是arr[0]第一个元素肯定是最小值。发现列表并不是有序的，
# 当时是这样啊，因为堆做的并不是把整个列表排好序，而是变成了一颗有规律的二叉树
#
# 假设有 n 个数据元素的序列 k0，k1，…，kn-1，当且仅当满足ki≤k2i+1 且 ki≤k2i+2（其中 i=0,2,...,(n-1)/2）时，
# 可以将这组数据称为小顶堆（小根堆）；或者满足 ki≥k2i+1 且 ki≥k2i+2（其中 i=0,2,...,(n-1)/2）时，可以将这组数据称为大顶堆（大根堆）。

# 使用方法2：heappush(heap, item)
heap = []
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
heapq.heappush(heap,5)
# heappush(heap, item)语句是将元素item压入堆中，且保持小顶堆的顺序
# 使用方法3： heappop(heap)
a = heapq.heappop(heap)
b = heapq.heappop(heap)
print(a, b)
# 使用方法4： heapreplace()
heapq.heapreplace(heap, 5)
# 使用方法5：heapq.nlargest(n, heap) 和  heapq.nsmallest(n, heap)
a = heapq.nsmallest(1, heap)
print(a)  # 返回的是列表哦
# 使用方法6： heapq.merge(*iterables, key=None, reverse=False)将多个有序的堆合成一个大的有序堆，然后在输出
heap2 = []
heapq.heappush(heap2, 4)
heapq.heappush(heap2, 3)
b = heapq.merge((heap, heap2))
print(b)
