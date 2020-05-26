"""
员工的重要性
给定一个保存员工信息的数据结构，它包含员工的唯一id,重要度和直系下属的id
# Employee info
"""
from typing import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

# DFS 递归实现
class Solution:
	def getImportance(self, employee: List['Employee'], id: int) -> int:
		employee_idMap = {e.id: e for e in employee}
		def dfs(eid):
			employee = employee_idMap[eid]
			return (employee.importance + sum(dfs(eid) for eid in employee.subordinates))
		return dfs(id)
		

# BFS 迭代实现 使用队列
class Solution:
	def getImportance(self, employees: List['Employee'], id:int)-> int:
		hashmap = {e.id:e for e in employees}
		queue = [id]
		while queue:
			cur = queue.pop(0)
			e = hashmap[cur]
			res+= e.importance
			for i in e.subordinates:
				queue.append(i)
		return res


solu = Solution()
a = Employee(1, 5, [2, 3])
b = Employee(2, 3, [])
c = Employee(3, 3, [])
ans = solu.getImportance([a, b, c], 1)
print(ans)

