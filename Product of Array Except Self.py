# Given an array nums of n integers where n > 1,  return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i]


class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []
        length = len(nums)
        answer = [0] * length

        answer[0] = 1

        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer

if __name__ == '__main__':

    arr = [1,2,3,4]
    solution = Solution()
    print(solution.productExceptSelf(arr))

# Instead of dividing the product of all the numbers in the array by the number at a given index
# to get the corresponding product, we can make use of the product of all the numbers to the left
# and all the numbers to the right of the index. Multiplying these two individual products
# would give us the desired result as well.

# input array = [1,2,3,4]
# left product= [1,1,2,6] (left product of 1 is 1 as there are no elements to the left of 1)
# right prod  = [24,12,4,1] (right --""-- right of 1)
# result array= [24,12,8,6]