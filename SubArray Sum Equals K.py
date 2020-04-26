import math

# Given an array of integers and an integer k, you need to find the total number of
# continuous subarrays whose sum equals to k

class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sum = 0
        sumMap = {}
        sumMap[0] = 1
        if len(nums)==0:
            return 0
        for i in nums:
            sum += i
            count += sumMap.get(sum-k,0)
            sumMap[sum] = sumMap.get(sum,0)+1

        return count



if __name__ == '__main__':

    arr = [1,1,1]
    solution = Solution()
    print(solution.subarraySum(arr,1))