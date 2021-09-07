from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # （1）按照结束时间对课程进行排序
        # （2）使用一个大顶堆来储存已经选择的课程的长度
        # （3）一旦发现安排了当前课程之后，其结束时间超过了最晚结束时间，那么就从已经安排的课程中，取消掉一门最耗时的课程
        courses = sorted(courses, key=lambda x:x[1])
        d = 0
        heap = []
        for course in courses:
            d += course[0]
            heapq.heappush(heap, -course[0])
            if d > course[1]:
                d += heapq.heappop(heap)
        return len(heap)


if __name__ == '__main__':
    solu = Solution()
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    ans = solu.scheduleCourse(courses)
    print(ans)