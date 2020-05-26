class Solution:
	def reverseWords(self, s:str) -> str:
		ans = s.lstrip().rstrip().split(' ')
		ans = [i for i in ans if i!='']
		print(ans)
		ans = [i for i in reversed(ans)]
		print(ans)
		str = ''
		for i in ans:
			str+=' '+i
		str = str.lstrip().lstrip()
		return str

solu = Solution()
ans = solu.reverseWords(" hello    world  ")
print(ans)