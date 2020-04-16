# Given a string containing only three types of characters: '(', ')' and '*', write a function
# to check whether this string is valid. We define the validity of a string by these rules
# 1.Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 2.Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 3.Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# 5. An empty string is also valid.


class Solution(object):
    def checkValidString(self, s):
        
        l = 0
        h = 0
        for c in s:
            l += 1 if c == "(" else -1
            h += 1 if c != ")" else -1
            if h < 0:
                return False
            l = max(l, 0)
        return l == 0


if __name__ == '__main__':

    solution = Solution()
    print(solution.checkValidString("(*)"))