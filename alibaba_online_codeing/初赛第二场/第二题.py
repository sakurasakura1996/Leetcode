class Solution:
    """
    @param triangle: Coordinates of three points
    @param point: Xiaoqi's coordinates
    @return: Judge whether you can cast magic
    """
    def castMagic(self, triangle, point):

        # write your code here
        point1 = triangle[0]
        point2 = triangle[1]
        point3 = triangle[2]

        def IsTrangleOrArea(x1, y1, x2, y2, x3, y3):
            return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

        def IsInside(x1, y1, x2, y2, x3, y3, x, y):
            # 三角形ABC的面积
            ABC = IsTrangleOrArea(x1, y1, x2, y2, x3, y3)
            # 三角形PBC的面积
            PBC = IsTrangleOrArea(x, y, x2, y2, x3, y3)
            if PBC == 0.0 and (x2 <= x <= x3 or x3 <= x <= x2) and (y2 <= y <= y3 or y3 <= y <= y2):
                return True
            # 三角形ABC的面积
            PAC = IsTrangleOrArea(x1, y1, x, y, x3, y3)
            if PAC == 0.0 and (x1 <= x <= x3 or x3 <= x <= x1) and (y1 <= y <= y3 or y3 <= y <= y1):
                return True
            # 三角形ABC的面积
            PAB = IsTrangleOrArea(x1, y1, x2, y2, x, y)
            if PAB == 0.0 and (x1 <= x <= x2 or x2 <= x <= x1) and (y1 <= y <= y2 or y2 <= y <= y1):
                return True
            return (ABC == PBC + PAC + PAB)

        xmin = min(point1[0], point2[0], point3[0])
        xmax = max(point1[0], point2[0], point3[0])
        ymin = min(point1[1], point2[1], point3[1])
        ymax = max(point1[1], point2[1], point3[1])

        if IsInside(point1[0], point1[1],point2[0], point2[1],point3[0], point3[1],point[0], point[1]) \
                and xmin <= point[0] <= xmax and ymin <= point[1] <= ymax:
            return "Yes"
        else:
            return "No"

solu = Solution()
triangle = [[0,0],[2,0],[2, 2]]
point= [2, 3]

ans = solu.castMagic(triangle, point)
print(ans)
