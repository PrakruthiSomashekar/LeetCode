
class Solution(object):
    def minStartValue(self, nums):

        minValue = 1
        i=0
        numsSum = minValue
        while i<len(nums):
            if numsSum+nums[i]<=0:
                minValue += 1
                numsSum = minValue
                i=0
            else:
                numsSum += nums[i]
                i += 1
        return minValue

if __name__ == '__main__':

    arr = [1,-2,-3]
    solution = Solution()
    print(solution.minStartValue(arr))