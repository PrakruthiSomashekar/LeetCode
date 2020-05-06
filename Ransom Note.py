# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        parentList = list(magazine)
        count = 0
        for i in range(len(ransomNote)):
            if parentList.__contains__(ransomNote[i]):
                parentList.remove(ransomNote[i])
                count += 1
        if count == len(ransomNote):
            return True
        else:
            return False

if __name__ == '__main__':

    solution = Solution()
    print(solution.canConstruct("a","b"))