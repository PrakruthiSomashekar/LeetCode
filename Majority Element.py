
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

import collections

class Solution(object):
    def majorityElement(self, nums):
        freq = collections.Counter(nums)
        for i in freq:
            if freq.get(i)>(len(nums)//2):
                return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2]))