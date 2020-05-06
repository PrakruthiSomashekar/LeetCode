
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

import collections

class Solution(object):
    def firstUniqChar(self, s):
        if s is None:
            return -1

        freq = collections.Counter(s)
        for i in range(len(s)):
            if freq.get(s[i])==1:
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar("loveleetcode"))