class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def solve(m):
            if m <= 1:
                return m
            maxt = (1 << (len(bin(m)) - 3))
            return (2*maxt-1) - solve(m-maxt)
        to_ret = solve(n)
        return to_ret