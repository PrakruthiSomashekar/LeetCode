
# Given a number, find if the sum of its digits after squaring itself iteratively becomes 1
# eg: 2->4->16->(1^2 + 2^2)=37->(3^2+7^2)->so on


class Solution(object):
    def isHappy(self, n):
        sum = self.getSumOfSquares(n)
        sumList = []
        sumList.append(sum)
        print(sum)
        while sum != 1:
            sum = self.getSumOfSquares(sum)
            if sumList.__contains__(sum):
                return False
            sumList.append(sum)
        return True

    def getSumOfSquares(self,number):
        sum = 0
        while number > 0:
            digit1 = number % 10
            number = number // 10
            sum += (digit1 ** 2)
        return sum


if __name__ == '__main__':

    solution = Solution()
    print(solution.isHappy(2))