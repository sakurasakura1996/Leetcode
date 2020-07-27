"""
https://mp.weixin.qq.com/s/UnfHolcYFeinOEipSet7rA
根据大佬推送来实现一波
冒泡排序；
选择排序；
插入排序；
希尔排序；
归并排序；
快速排序；
堆排序；
计数排序；
桶排序；
基数排序。
"""

class Sort:
    def BubbleSort(self, array):
        """
        基本原理
        比较类排序算法。算法描述如下(假设是升序排序)：
        比较相邻的元素，如果第一个元素比第二个大，就交换它们；
        对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
        针对所有的元素重复以上的步骤，除了最后已经选出的有序元素；
        持续对剩下的无序元素重复上面的步骤，直到排序完成。
        算法时间复杂度 O(n^2)
        """
        if not array:
            return array
        length = len(array)
        for i in range(length):
            for j in range(length-i-1):
                if array[j] > array[j+1]:
                    array[j+1], array[j] = array[j], array[j+1]  # python可以直接交换过来
        return array

    def SelectionSort(self,array):
        """
        选择排序
        基本原理
        比较类排序算法。算法描述如下(假设是升序排序)：
        首先在未排序序列中找到最小元素，存放到排序序列的起始位置；
        再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾；
        重复第二步，直到所有元素均排序完毕。
        算法时间复杂度：O(n^2)
        """
        if not array:
            return array
        length = len(array)
        for i in range(length-1):
            idx_min = i
            for j in range(i+1, length):
                if array[j] < array[idx_min]:
                    idx_min = j
            array[i], array[idx_min] = array[idx_min],array[i]
        return array

    def InsertSort(self, array):
        """
        插入排序
        比较类排序算法。算法描述如下(假设是升序排序)：
        从第一个元素开始，该元素可以认为已经被排序；
        取出下一个元素，在已经排序的元素序列中从后向前扫描；
        如果该元素(已排序)大于新元素，将该元素移到下一位置；
        重复第三步，直到找到已排序的元素小于或等于新元素的位置；
        将新元素插入到该位置；
        重复第二到第五步，直到排序完成。
        算法时间复杂度 O(n^2)
        """
        if not array:
            return array
        length = len(array)
        for i in range(1, length):
            pointer, cur = i-1, array[i]
            while pointer >= 0 and array[pointer] > cur:
                array[pointer+1] = array[pointer]
                pointer -= 1
            array[pointer+1] = cur
        return array

    def ShellSort(self, array):
        """
        希尔排序
        基本原理
        比较类排序算法。其基本思想是把数据按下标的一定增量分组，对每组使用直接插入排序算法排序，随着增量逐渐减少，每组包含的数越来越多，
        当增量减至1时，整个文件恰被分成一组，算法终止。算法描述如下(假设是升序排序)：
        选择一个增量序列  t1,t2,...tk, tk=1；
        按增量序列个数k，对序列进行k次排序；
        每次排序，根据对应的增量ti，将待排序列分割成若干长度为m的子序列，分别对各子序列进行直接插入排序。
        希尔排序不够熟悉
        """
        if not array:
            return array
        length = len(array)
        gap = length // 2
        while gap > 0:
            for i in range(gap,length):
                j, cur = i, array[i]
                while (j - gap >= 0) and (cur < array[j - gap]):
                    array[j] = array[j - gap]
                    j = j - gap
                array[j] = cur
            gap = gap // 2
        return array

    def MergeSort(self, array):
        """
        归并排序
        比较类排序算法。该算法采用了分治法的思想，将已有序的子序列合并，得到完全有序的序列。算法描述如下(假设是升序排序)：
        把长度为n的输入序列分为两个长度为n/2的子序列；
        对这两个子序列分别采用归并排序；
        将两个排序好的子序列合并成一个最终的排序序列。
        算法时间复杂度 O(nlogn)
        """
        def Merge(array1, array2):
            result = []
            while array1 and array2:
                if array1[0] < array2[0]:
                    result.append(array1.pop(0))
                else:
                    result.append(array2.pop(0))
            if array1:
                result.extend(array1)
            if array2:
                result.extend(array2)
            return result

        if not array or len(array) < 2:
            return array
        pointer = len(array) // 2
        left = array[:pointer]
        right = array[pointer:]
        return Merge(self.MergeSort(left), self.MergeSort(right))

    def QuickSort(self, array, left, right):
        """
        快排
        比较类排序算法。基本思想是通过一次排序将待排序数据分隔成独立的两部分，其中一部分数据均比另一部分的数据小。
        然后分别对这两部分数据继续进行排序，直到整个序列有序。算法描述如下(假设是升序排序)：
        从数列中挑出一个元素，称为“基准”；
        重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆放在基准的后面(相同的数可以到任一边)；
        分别对步骤二中的两个子序列再使用快速排序；
        重复上述步骤，直到排序完成。
        """
        if left >= right:
            return array
        pivot, i, j = array[left], left, right
        while i < j:
            while i < j and array[j] >= pivot:
                j -= 1
            array[i] = array[j]
            while i < j and array[i] <= pivot:
                i += 1
            array[j] = array[i]
        array[j] = pivot
        self.QuickSort(array, left, i-1)
        self.QuickSort(array, i+1, right)
        return array

    def QuickSort2(self,array, left, right):
        # 上面的快排写法挺好的，但不是最最正统的写法哈哈哈，应该另外定义一个partition函数，这个函数才是核心处理功能
        def partition(array, head, tail):



            pivot = array[head]
            while head < tail:
                while head < tail and array[tail] >= pivot:
                    tail -= 1
                array[head] = array[tail]
                while head < tail and array[head] <= pivot:
                    head += 1
                array[tail] = array[head]
            array[head] = pivot
            return head

        if left < right:
            mid = partition(array, left, right)
            self.QuickSort2(array,left, mid-1)
            self.QuickSort2(array,mid+1, right)
        return array

    def heapify(self, array, length, i):
        """
        堆化
        将初始待排序序列构建成大顶堆，此堆为初始的无序区；将堆顶元素和最后一个元素交换，此时得到的新的无序区

        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < length and array[largest] < array[left]:
            largest = left
        if right < length and array[largest] < array[right]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.heapify(array, length, largest)

    def HeapSort(self,array):
        # 堆排序
        length = len(array)
        for i in range(length, -1, -1):
            self.heapify(array, length, i)
        for i in range(length-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array

    def RadixSort(self, array):
        # 基数排序
        max_value = max(array)
        num_digits = len(str(max_value))
        for i in range(num_digits):
            buckets = [[] for k in range(10)]
            for j in array:
                buckets[int(j / (10 ** i)) % 10].append(j)
            output = [m for bucket in buckets for m in bucket]
        return output








sorter = Sort()
array = [3, 5, 1, 5, 3, 6]
ans = sorter.RadixSort(array)
print(ans)
