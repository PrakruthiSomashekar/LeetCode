import math

# Kadane's Algorithm
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



class Solution(object):
    def maxSubArray(self, nums):
        maxSum = -math.inf
        nextSum = 0

        for i in nums:

            nextSum = max(i, nextSum + i)
            if(nextSum > maxSum):
                maxSum = nextSum

        return maxSum



if __name__ == '__main__':

    arr = [2,3]
    solution = Solution()
    print(solution.maxSubArray(arr))