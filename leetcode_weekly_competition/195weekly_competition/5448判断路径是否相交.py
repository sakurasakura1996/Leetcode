"""
给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。
机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。
如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。

示例 1：
输入：path = "NES"
输出：false
解释：该路径没有在任何位置相交。
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        if not path:
            return False
        step_dict = {'N':[0,1],
                  'S':[0,-1],
                  'W':[-1,0],
                  'E':[1,0]}
        posi = [0,0]
        ans = [[0,0]]
        for i in path:
            posi[0] += step_dict[i][0]
            posi[1] += step_dict[i][1]
            if posi in ans:
                return True
            else:
                ans.append([posi[0],posi[1]])
        return False


solu = Solution()
path = "NESWW"
ans = solu.isPathCrossing(path)
print(ans)


