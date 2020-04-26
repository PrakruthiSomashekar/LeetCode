import math

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers
# in this range, inclusive

# Brian Kernighan's algorithm. - goes through as many iterations as there are number of set bits


class Solution(object):
    def rangeBitwiseAnd(self, m, n):

        while n>m:
            n = n & n-1
        return m&n


if __name__ == '__main__':

    solution = Solution()
    print(solution.rangeBitwiseAnd(5,7))