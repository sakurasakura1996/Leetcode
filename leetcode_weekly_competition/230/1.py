from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n = len(items)
        ans = 0
        if ruleKey == "type":
            for item in items:
                type = item[0]
                if type == ruleValue:
                    ans += 1
        elif ruleKey == "color":
            for item in items:
                type = item[1]
                if type == ruleValue:
                    ans += 1
        else:
            for item in items:
                type = item[2]
                if type == ruleValue:
                    ans += 1
        return ans





if __name__ == '__main__':
    solu = Solution()
