from typing import List
import math
class Solution:
    # 总体思路就是转换成角度之后，然后排序，再利用双指针来做。还有个问题就是注意当视角跨过x轴向右的时候，
    # 这个时候看到的点会包含角度最小的那部分点 以及 角度最大的那些点， 处理的trick就是将整个序列加上360度之后
    # 再append到原始的序列上，然后起始的下标l从 0 - len(points)-1。
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        to_ret_base = 0
        to_ret = 0
        lx, ly = location
        pts = []
        for x, y in points:
            if x == lx and y == ly:
                to_ret_base += 1
                continue
            db = y-ly
            lb = x-lx
            if lb == 0 and db > 0:
                pts.append(90)
            elif lb == 0 and db < 0:
                pts.append(-90)
            elif lb < 0:
                lb = -lb
                arg = math.atan(db/lb)
                to_append = arg/math.pi*180
                if to_append > 0:
                    to_append = 90 + 90 - to_append
                elif to_append < 0:
                    to_append = -90 + -90 - to_append
                else:
                    to_append = 180
                pts.append(to_append)
            else:  # lb > 0
                arg = math.atan(db/lb)
                pts.append(arg/math.pi*180)
        pts = sorted(pts)
        pts = pts + [t+360 for t in pts]
        # print(pts)
        # 这里的表达实在牛逼，看似简单程序，但是我理解就理解了好半天，大佬在所有点的角度列表上，所有元素又加了360度，为的就是让代码中
        # pts[s] + angle可以直接表达题意，意思就是可以搞出一个环来。这个表达很像双指针和快慢指针。
        s, e = -1, 0
        while e < len(pts):
            s += 1
            while e < len(pts) and pts[e] <= pts[s] + angle:
                e += 1
            to_ret = max(e-s, to_ret)
        return to_ret + to_ret_base