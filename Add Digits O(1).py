
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# Congruence formula: 1 + (n-1)%(base-1) where base=10

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1+((num-1)%9)


if __name__ == '__main__':
    solution = Solution()
    print(solution.addDigits(38))