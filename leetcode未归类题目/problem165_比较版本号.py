class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_nums = [int(num) for num in version1.split(".")]
        version2_nums = [int(num) for num in version2.split(".")]
        m = len(version1_nums)
        n = len(version2_nums)
        if m < n:
            for i in range(n - m):
                version1_nums.append(0)
        elif m > n:
            for i in range(m - n):
                version2_nums.append(0)
        for i in range(len(version2_nums)):
            if version1_nums[i] < version2_nums[i]:
                return -1
            elif version1_nums[i] > version2_nums[i]:
                return 1
            else:
                continue
        return 0

if __name__ == '__main__':
    solu = Solution()
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    ans = solu.compareVersion(version1, version2)
    print(ans)
