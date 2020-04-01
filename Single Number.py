import collections

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.



class Solution(object):
    def singleNumber(self, nums):

        freq = collections.Counter(nums)

        for key in freq:
            if freq[key] == 1:
                print(key)


if __name__ == '__main__':

    arr = [2,2,1,4,1]
    solution = Solution()
    solution.singleNumber(arr)