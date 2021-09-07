
import sys
if __name__ == '__main__':
    m, n = sys.stdin.readline().strip().split()
    nums = sys.stdin.readline().strip().split()
    digits = []
    chars = []
    for num in nums:
        if num.isdigit():
            digits.append(num)
        else:
            chars.append(num)
    digits.sort()
    chars.sort()
    numbers = []

    def backtrace(cur, path, l):
        if len(cur) == l:
            numbers.append(''.join(sorted(cur).copy()))
        for i, item in enumerate(path):
            cur.append(item)
            temp = path[:i] + path[i+1:]
            backtrace(cur, temp, l)
            cur.pop()
        return numbers


    ans = []
    for i in range(1, int(m)-1):
        # i 表示数字的长度
        numbers = []
        numbers = backtrace([], digits, i)
        digit_tmp = numbers.copy()
        numbers = []
        numbers = backtrace([], chars, int(m)-i)
        num_tmp = numbers.copy()
        for digit in digit_tmp:
            for num in num_tmp:
                ans.append(digit+num)

    ans.sort()
    ans = set(ans)
    ans = list(ans)
    ans.sort()
    print(ans)






