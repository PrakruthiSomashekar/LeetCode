import collections

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.



class Solution(object):
    def countElements(self, arr):
        count=0
        for num in arr:
            if arr.__contains__(num+1):
                count += 1
        return count


if __name__ == '__main__':

    arr = [1,1,2]
    solution = Solution()
    print(solution.countElements(arr))