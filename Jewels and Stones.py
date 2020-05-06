
# You're given strings J representing the types of stones that are jewels, and S representing
# the stones you have.  Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

import collections
class Solution(object):
    def numJewelsInStones(self, J, S):
       freq = collections.Counter(S)
       count = 0
       for i in range(len(J)):
           if J[i] in freq:
               count += freq.get(J[i])
       return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones("aA","aAAbbbb"))