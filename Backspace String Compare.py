
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

class Solution(object):
    def backspaceCompare(self, S, T):

        str1 = self.getString(S)
        str2 = self.getString(T)

        return True if str1 == str2 else False

    def getString(self, S):
        l1 = []
        for i in range(len(S)):
            if S[i] != '#':
                l1.append(S[i])
            elif len(l1) != 0:
                l1.pop()

        ans=""
        while len(l1)!=0:
            ans += l1[0]
            l1.pop(0)
        return ans


if __name__ == '__main__':

    solution = Solution()
    print(solution.backspaceCompare("ab#d","ad#d"))