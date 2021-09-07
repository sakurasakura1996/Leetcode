import sys

class Solution:
    def helloWorld(self, s):
        print("hello,"+s)
        print(s)


if __name__ == '__main__':
    solu = Solution()
    for line in sys.stdin:
        s = line
        solu.helloWorld(s)