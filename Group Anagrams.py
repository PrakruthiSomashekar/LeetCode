import ast

# Given an array of strings, group anagrams together.



class Solution(object):
    def groupAnagrams(self, strs):
        anagramMap = {}
        anagramList = []
        for i in strs:
            anagram = "".join(sorted(i))
            if anagram not in anagramMap.keys():
                anagramMap[anagram] = [i]
            else:
                existingList = anagramMap.get(anagram)
                existingList.append(i)
                anagramMap.update({anagram:existingList})


        for alist in anagramMap:
            anagramList.append(anagramMap[alist])

        return anagramList



if __name__ == '__main__':

    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(arr))