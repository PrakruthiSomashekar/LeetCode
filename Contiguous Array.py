import collections

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1

class Solution(object):
    def findMaxLength(self, nums):

        count = 0
        maxLen = 0
        countMap = {}
        # if the array is empty, count=0 and index=-1 as we haven't seen it yet
        countMap.update({0: -1})

        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            if countMap.__contains__(count):
                
                maxLen = max(maxLen, i-countMap.get(count))
            else:
                countMap.update({count:i})

        return maxLen


if __name__ == '__main__':
    arr = [0,1]
    solution = Solution()
    print(solution.findMaxLength(arr))