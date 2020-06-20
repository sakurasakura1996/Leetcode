from typing import List
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        arr_len = len(arr)
        arr.sort()
        medium = arr[int((arr_len - 1) / 2)]
        left = 0
        right = arr_len-1
        num = 0  # 用于记录输出了几个答案了
        ans = []
        while left <= right and num<k:
            if abs(arr[left]-medium) > abs(arr[right]-medium):
                ans.append(arr[left])
                num += 1
                left += 1
            elif abs(arr[left]-medium) == abs(arr[right]-medium):

                if arr[left] > arr[right]:
                    ans.append(arr[left])

                    left += 1
                else:
                    ans.append(arr[right])
                    right -= 1
                num += 1
            else:
                ans.append(arr[right])
                right -= 1
                num+= 1
        return ans

solu = Solution()
arr = [6,7,11,7,6,8]
k = 5
ans = solu.getStrongest(arr, k)
print(ans)
