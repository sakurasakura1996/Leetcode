"""
1108.IP地址无效化
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
示例 1：
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
示例 2：
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
给出的 address 是一个有效的 IPv4 地址
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        str_list = address.split('.')
        for i in range(len(str_list)-1):
            str_list[i] = str_list[i] + "[.]"
        return "".join(str_list)


solu = Solution()
address = "255.100.50.0"
ans = solu.defangIPaddr(address)
print(ans)