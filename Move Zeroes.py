
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.



class Solution(object):
    def moveZeroes(self, nums):
        nonZeroIndex = 0
        i = 0

        while i < len(nums):
            if(nums[i] != 0):
                nums[nonZeroIndex],nums[i] = nums[i], nums[nonZeroIndex]
                nonZeroIndex += 1
            i += 1
        return nums



if __name__ == '__main__':

    arr = [0,1,0,3,12]
    solution = Solution()
    print(solution.moveZeroes(arr))