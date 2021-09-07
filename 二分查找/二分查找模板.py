"""
二分查找主要有三个问题，一个是查找数组中目标值的位置，这是最简单的： problem704
                   一个是，数组中元素有重复值，找到目标值的左边界
                   还有一个就是上面的情况，然后找到右边界
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int):
        """
        查找元素的话还是挺简单的，我们这里定义好模板，以后就按照这个思路来写就行了，left=0，right=len(nums)-1能取到
        这样的话，我们的while循环判断就定下来了，跳出循环的条件必须是 left > right了，所以left == right要继续执行
        所以while 循环后面应该接 <= . 后面几种情况不难分析，然后return也不难。
        """
        if not nums:
            return -1
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return -1

    def searchLeftRange(self, nums: List[int], target: int) -> int:
        """
        nums数组有重复元素，查找到目标值的左边界，如果没有目标值返回-1
        这个问题和找有边界是一样的，就比较复杂了。
        我们定义left = 0，right = len(nums),也就是查找区间是左闭右开的，这个时候 left = right的时候，就可以推出循环了
        所以 while循环的判断就是 while left < right: 后面的分析就在代码里面说吧。
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums)
        while left < right:
            # 这里我们一定要记得，循环退出的时候，一定是left==right，所以return left和right都可以，
            # 并且，在分析后面left，right取值的时候，可以举个例子来看，就是right = left + 1的时候。
            # 比如      left   right
            #            |      |
            #            7      8
            # 我们可以就考虑上面的情况，记得考虑两种情况，就是target = 7，或者 target = 8 的情况。
            # 可以发现，最后，left只要往左移动，就可以了。
            mid = left + (right - left) // 2
            # 师弟说这种情况是不需要单独判断 nums[mid] == target的，确实。
            if nums[mid] < target:
                left = mid + 1   # notice:
            else:
                right = mid        # notice 我们要注意，这里的right = mid并不是说就取不到了。取不到的概念
                # 我们只用考虑在while循环判断那里有没有等于号就行。
        if left == len(nums) or nums[left] != target:
            return -1
        return left

    def searchLeftRange2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1    # 如果right = len(nums) - 1的话，我们后面就要想清楚，return 返回值是什么了。
        while left <= right:
            mid = left + (right - left) // 2
            # 这下面怎么思考，还是可以根据上面方法的例子来想。
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left == len(nums) or nums[left] != target:
            return -1
        return left

    def searchRightRange(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right - 1  # 或者 left - 1 是一样的

    def searchRightRange2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right  # 或者返回left - 1


if __name__ == '__main__':
    solu = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    ans1 = solu.searchRightRange2(nums, target)
    print(ans1)



