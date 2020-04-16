
# Given an array of non-negative integers, you are initially positioned at the first index
# of the array. Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        i = 0
        max_index = nums[i]
        while i < len(nums) and i <= max_index:
            new_index = nums[i] + i
            max_index = max(max_index, new_index)
            i += 1
        if i == len(nums):
            return True
        else:
            return False




if __name__ == '__main__':
    arr = [3,2,1,0,4]
    solution = Solution()
    print(solution.canJump(arr))