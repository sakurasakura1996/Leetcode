"""
一个王国里住着国王、他的孩子们、他的孙子们等等。每一个时间点，这个家庭里有人出生也有人死亡。
这个王国有一个明确规定的皇位继承顺序，第一继承人总是国王自己。我们定义递归函数 Successor(x, curOrder) ，给定一个人 x 和当前的继承顺序，该函数返回 x 的下一继承人。
Successor(x, curOrder):
    如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
        如果 x 是国王，那么返回 null
        否则，返回 Successor(x 的父亲, curOrder)
    否则，返回 x 不在 curOrder 中最年长的孩子
比方说，假设王国由国王，他的孩子 Alice 和 Bob （Alice 比 Bob 年长）和 Alice 的孩子 Jack 组成。

一开始， curOrder 为 ["king"].
调用 Successor(king, curOrder) ，返回 Alice ，所以我们将 Alice 放入 curOrder 中，得到 ["king", "Alice"] 。
调用 Successor(Alice, curOrder) ，返回 Jack ，所以我们将 Jack 放入 curOrder 中，得到 ["king", "Alice", "Jack"] 。
调用 Successor(Jack, curOrder) ，返回 Bob ，所以我们将 Bob 放入 curOrder 中，得到 ["king", "Alice", "Jack", "Bob"] 。
调用 Successor(Bob, curOrder) ，返回 null 。最终得到继承顺序为 ["king", "Alice", "Jack", "Bob"] 。
通过以上的函数，我们总是能得到一个唯一的继承顺序。

请你实现 ThroneInheritance 类：

ThroneInheritance(string kingName) 初始化一个 ThroneInheritance 类的对象。国王的名字作为构造函数的参数传入。
void birth(string parentName, string childName) 表示 parentName 新拥有了一个名为 childName 的孩子。
void death(string name) 表示名为 name 的人死亡。一个人的死亡不会影响 Successor 函数，也不会影响当前的继承顺序。你可以只将这个人标记为死亡状态。
string[] getInheritanceOrder() 返回 除去 死亡人员的当前继承顺序列表。
示例：
输入：
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
输出：
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]
解释：
ThroneInheritance t= new ThroneInheritance("king"); // 继承顺序：king
t.birth("king", "andy"); // 继承顺序：king > andy
t.birth("king", "bob"); // 继承顺序：king > andy > bob
t.birth("king", "catherine"); // 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew"); // 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // 继承顺序：king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]
提示：
1 <= kingName.length, parentName.length, childName.length, name.length <= 15
kingName，parentName， childName 和 name 仅包含小写英文字母。
所有的参数 childName 和 kingName 互不相同。
所有 death 函数中的死亡名字 name 要么是国王，要么是已经出生了的人员名字。
每次调用 birth(parentName, childName) 时，测试用例都保证 parentName 对应的人员是活着的。
最多调用 105 次birth 和 death 。
最多调用 10 次 getInheritanceOrder 。
"""
from typing import List
from collections import defaultdict
class ThroneInheritance:
    # 这道题目，感觉倒不是很难，就是题目太长，建议看示例：就是先生的孩子先继承皇位，他的儿子也比自己的叔叔先继承皇位。
    def __init__(self, kingName: str):
        self.d = defaultdict(list)
        self.dead = set()
        self.k = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.d[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(name):
            # 这里是最难想的，为什么要加上一个name是否在self.d的判断呢，因为如果我们遍历到了底端，也就是没有子嗣的节点时，要结束然后返回啊
            if name not in self.d:
                if name in self.dead:
                    return []
                else:
                    return [name]
            if name in self.dead:
                ans = []
            else:
                ans = [name]
            for i in self.d[name]:
                ans += dfs(i)
            return ans
        return dfs(self.k)


# 还有一个题解利用自定义的树结构来解决问题。其实解题思路同上面是一样的。
class FamilyTreeNode:
    def __init__(self, name):
        self.name = name
        self.chs = []   # 孩子节点
        self.alive = True


class FamilyTree:
    def __init__(self, name):
        self.root = FamilyTreeNode(name)
        self.family = {name: self.root}  # 利用哈希表加速查询

    def birth(self, parentName, childName):
        ch = FamilyTreeNode(childName)
        fa = self.family[parentName].chs.append(ch)
        self.family[childName] = ch

    def death(self, name):
        self.family[name].alive =False


class ThroneInheritan:

    def __init__(self, kingName: str):
        self.tree = FamilyTree(kingName)

    def birth(self, parentName: str, childName: str):
        self.tree.birth(parentName, childName)

    def death(self, name: str):
        self.tree.death(name)

    def getInherttance(self) -> List[str]:
        res = []

        def dfs(node):
            nonlocal res
            if node is None:
                return
            if node.alive:
                res += [node.name]
            for ch in node.chs:
                dfs(ch)

        dfs(self.tree.root)
        return res


