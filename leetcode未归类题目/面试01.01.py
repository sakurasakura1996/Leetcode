"""
判定字符是否唯一
实现一个算法，确定一个字符串s的所有字符是否全都不同
"""
class Solution:
	def isUnique(self, astr: str) -> bool:
		a = set()
		for i in range(len(astr)):
			a.add(astr[i])
		if len(astr) == len(a):
			return True
		return False

# 集合set的操作，添加元素add， remove移除指定元素
# update是讲字符串中的拆分成字符进行追加
# add，是当做整体追加在集合中
# 
