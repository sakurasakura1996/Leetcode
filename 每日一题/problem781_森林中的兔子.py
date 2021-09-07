from typing import List
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # 我们来理清下思路：我们应该要统计 answers中不同数值的个数，比如 值为num的个数为 x，那么其实num+1个数可以直接去掉，记为
        # num+1个兔子。如果x>=num+1,那么x直接剪掉，如果x < num+1，那么x直接就清0了。
        answers_counter = Counter(answers)
        ans = 0
        for num, x in answers_counter.items():
            while x > 0:
                ans += (num+1)
                x -= (num+1)
        return ans

if __name__ == '__main__':
    solu = Solution()
    answers = []
    ans = solu.numRabbits(answers)
    print(ans)