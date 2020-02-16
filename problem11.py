"""
盛最多水的容器
如果用最暴力的方法，那就是计算任意两个数作为答案可以容纳的水，然后
找到最大值作为结果输出，这样的时间复杂度为 n²,结果运行出来的结果是时间超时，所以要寻找更优速度

然后我发现了一个规律，左边的那个值，如果大小再下降，那么就直接跳过就可以了，右边的那个值，如果大小再
上升，那么这个值也可以跳过就行了。可以仔细想想是不是这样。 可是结果还是时间超时，妈的我太蠢了

看到别人说的双指针法，发现上面的解法已经有点接近了，但还是不如双指针来的简单，上面的复杂度还是n²的复杂度
双指针法：也就是在起始端和末端都安排一个指针，然后两个指针分别根据情况来向内侧移动，不断计算容器大小来
更新最大值，这样指针交错就可以结束遍历了，这样的话时间复杂度就只有 O(n)了
这次方法终于时间通过了，代码中还可以详细添加判断条件，如果右移的值还没有左边大，那么就不用计算本次容器值了，同样的
如果左移的值还没有右边大，那也不用计算本次容器值了。因为不可能大于当前的最大值


"""


from typing import List
# way 1
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max = 0
#         for i in range(len(height)-1):
#             # 用冒泡排序的方式来分别计算容器体积
#             for j in range(i+1,len(height)):
#                 num = min(height[i], height[j]) * (j-i)
#                 if num > max:
#                     max = num
#         return max

# way 2
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max = 0
#         for i in range(len(height)-1):
#             # 如果它比左边的数小,那么直接跳到下次循环
#             if i > 0 and height[i] < height[i-1]:
#                 continue
#             for j in range(i+1,len(height)):
#                 # 如果它右边的数比它大，那么这个数也可以直接跳过了
#                 if j < len(height)-1 and height[j] < height[j+1]:
#                     continue
#                 num = min(height[i], height[j]) * (j-i)
#                 if num > max:
#                     max = num
#         return max


# way3

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max = min(height[0], height[len(height) - 1]) * (right - left)
        while left < right:
            # 循环终止条件如上
            if height[left] < height[right]:
                # 左边的值限制了容器大小，则左指针往右移动，并且可以加上条件，如果右移的值
                # 如果右移的值还没有左边大，那么就不用计算本次容器值了，
                left = left +1
                # while height[left] < height[left+1] and (left+1)<right:
                #     left = left +1
                num = min(height[left], height[right]) * (right-left)
                if num>max:
                    max = num
            else:
                # 右边的值限制了容器大小，右指针往左移动，并且加上条件，如果左移的值
                # 如果左移的值还没有右边大，那也不用计算本次容器值了。因为不可能大于当前的最大值
                right = right -1
                # while height[right] > height[right-1] and (right-1)>left:
                #     right = right -1
                num = min(height[left], height[right]) * (right - left)
                if num > max:
                    max = num
        return max

a = [1,8,6,2,5,4,8,3,7]
solu = Solution()
answer = solu.maxArea(a)
print(answer)

