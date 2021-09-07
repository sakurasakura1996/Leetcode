from collections import defaultdict
class Solution:
    # 在已知使用滑动窗口方法的基础上来做这道题，貌似感觉并不难。
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        left = right = 0
        window = defaultdict(int)
        ans = 0
        while right < n:
            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
            right += 1
            ans = max(ans, len(window))
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "pwwkew"
    ans = solu.lengthOfLongestSubstring(s)
    print(ans)