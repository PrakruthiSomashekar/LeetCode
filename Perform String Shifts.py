from collections import deque

# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

class Solution(object):
    def stringShift(self, s, shift):
        stringList = deque(list(s))
        for i in range(len(shift)):
            if shift[i][0] == 0:
                stringList.rotate(-shift[i][1])
            else:
                stringList.rotate(shift[i][1])
        return "".join(stringList)


if __name__ == '__main__':

    arr = [[1,1],[1,1],[0,2],[1,3]]
    solution = Solution()
    print(solution.stringShift("abcdefg",arr))
