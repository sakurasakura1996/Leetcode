from typing import List
from collections import deque
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # 那就直接遍历该节点呗
        mp = {employee.id: employee for employee in employees}

        def dfs(idx: int) -> int:
            employee = mp[idx]
            total = employee.importance + sum(dfs(subIdx) for subIdx in employee.subordinates)
            return total
        return dfs(id)

    def getImportance2(self, employees: List[Employee], id: int) -> int:
        # BFS 遍历
        mp = {employee.id: employee for employee in employees}
        queue = deque()
        queue.append(mp[id])
        ans = 0
        while queue:
            employee = queue.popleft()
            ans += employee.importance
            for subIdx in employee.subordinates:
                queue.append(mp[subIdx])
        return ans

if __name__ == '__main__':
    solu = Solution()
    employees = []
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])
    employees.append(e1)
    employees.append(e2)
    employees.append(e3)
    ans = solu.getImportance2(employees, 1)
    print(ans)