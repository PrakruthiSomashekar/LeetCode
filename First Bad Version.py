# You are given an API bool isBadVersion(version) which will return whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

def isBadVersion(version):
    arr = [0,0,0,0,1,1,1]
    return arr[version] == 1

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left<right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left

if __name__ == '__main__':
    solution = Solution()
    print(solution.firstBadVersion(4))