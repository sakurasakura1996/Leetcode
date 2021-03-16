from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 这道题目当时做的时候没做出来，现在 印象还挺深的
        people.sort(key=lambda x:(-x[0], x[1]))
        n = len(people)

        ans = []
        for person in people:
            height, number = person[0], person[1]
            if len(ans) <= number:
                ans.append(person)
            else:
                ans.insert(number, person)
        # 下面的写法更加巧妙，还不是很熟悉
        # for person in people:
        #     ans[person[1]:person[1]] = [person]
        # 上面这种表达方法就类似于，ans[1:2] 应该是 List[List[int]]的样式
        return ans




if __name__ == '__main__':
    solu = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ans = solu.reconstructQueue(people)
    print(ans)
