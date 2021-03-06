"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from functools import lru_cache
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        n = len(s)
        if n < 4 or n > 12:
            return []

        @lru_cache
        def dfs(idx,j):
            # idx表示从s的idx开始算，然后j表示的是几段，题目是分成四段，那么dfs()返回的就是从s[idx]开始是否能拼成j段有效的ip地址
            if idx < n and j > 0 and int(s[idx]) == 0:
                if dfs(idx+1, j-1):
                    return '0.'+ dfs(idx+1, j-1)
            elif idx < n and j > 0 and int(s[idx]) > 2:
                if dfs(idx+1, j-1):
                    return s[idx] + dfs(idx+1, j-1)
                return None


        