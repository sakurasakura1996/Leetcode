"""
841. 钥匙和房间
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。
钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
最初，除 0 号房间外的其余所有房间都被锁住。
你可以自由地在房间之间来回走动。
如果能进入每个房间返回 true，否则返回 false。
示例 1：
输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。

示例 2：
输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
提示：
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
所有房间中的钥匙数量总计不超过 3000。
"""
# 想利用回溯或者BFS来写
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        def backtrack(nums, tmp):
            if len(tmp) == n:
                return True
            # nums可选择的列表，tmp是已经走过的路径可以用列表来存储字典呢？
            for num in nums:
                if num not in tmp:
                    tmp.append(num)
                    backtrack(rooms[num], tmp)
            return

        tmp = [0]
        backtrack(rooms[0], tmp)
        return len(tmp) == n

    def canVisitAllRooms_2(self, rooms: List[List[int]])-> bool:
        n = len(rooms)
        from collections import deque, defaultdict
        visited = defaultdict(int)
        visited[0] = 1
        queue = deque([0])
        while queue:
            cur = queue.popleft()
            for room in rooms[cur]:
                if room not in visited:
                    visited[room] = 1
                    queue.append(room)
        return len(visited) == n


solu = Solution()
rooms = [[1],[2],[3],[]]
ans = solu.canVisitAllRooms_2(rooms)
print(ans)
