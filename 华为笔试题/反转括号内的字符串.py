import sys
if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    def recur(ss: str):
        if not ss:
            return ss
        left = 0
        right = len(ss) - 1
        ans_left = ans_right = ""
        while left <= right:
            while left <= right and ss[left] != '(':
                ans_left += ss[left]
                left += 1
            while left < right and ss[right] != ')':
                ans_right = ss[right] + ans_right
                right -= 1
            if left < right:
                return ans_right + recur(ss[left+1:right]) + ans_left
            else:
                return ans_right + ans_left
    ans = recur(s)
    print(ans)









