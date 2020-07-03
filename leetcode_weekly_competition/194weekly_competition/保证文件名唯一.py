"""
给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，
其中 k 是能保证文件名唯一的 最小正整数 。
返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。
示例 1：
输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：文件系统将会这样创建文件名：
"pes" --> 之前未分配，仍为 "pes"
"fifa" --> 之前未分配，仍为 "fifa"
"gta" --> 之前未分配，仍为 "gta"
"pes(2019)" --> 之前未分配，仍为 "pes(2019)"
"""
# from typing import List
# class Solution:
#     def getFolderNames(self, names: List[str]) -> List[str]:
#         names_dict = {}
#         for i in range(len(names)):
#             if names[i] in names_dict:
#                 cur_name = names[i] +"(1)"
#                 num = 2
#                 while cur_name in names_dict:
#                     cur_name = names[i] + "("+str(num)+")"
#                     num += 1
#                 names[i] = cur_name
#
#             names_dict[names[i]] = i
#         return names
# 上述方法超出时间限制
# 大佬的答案如下，和我上面解法相似，我当时想改进的地方也就是这里的num，每次都是从1开始，太慢了
import collections
from typing import List
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        label = collections.Counter()
        occ = set()
        ans = list()
        for name in names:
            if name not in occ:
                ans.append(name)
                occ.add(name)
                label[name] = 1
            else:
                # l = 1 if name not in label else label[name]
                l = label[name]
                mask = name + "(%d)"
                while True:
                    upd = mask % l
                    if upd not in occ:
                        ans.append(upd)
                        occ.add(upd)
                        label[name] = l + 1
                        break
                    l += 1
        return ans
# way2 此方法写错了，卧槽，这次只做出来了一题
from typing import List
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # 先用字典来存储需要改动的name的位置索引，然后在统一往上加
        from collections import defaultdict
        names_dict = defaultdict(list)
        for i in range(len(names)):
            names_dict[names[i]].append(i)
        a_dict = {}
        for key,value in names_dict.items():
            value_len = len(value)
            if value_len > 1:
                num = 1
                cur_name = names[0]
                for i in range(1, value_len):
                    while cur_name in names_dict or cur_name in a_dict:
                        cur_name = key + "("+str(num)+")"
                        num += 1
                    names[value[i]] = cur_name
                    a_dict[cur_name] = value[i]
        return names


solu = Solution()
names = ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
ans = solu.getFolderNames(names)
print(ans)
