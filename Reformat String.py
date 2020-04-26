
import itertools


class Solution(object):
    def reformat(self, s):
        string = ""
        if not s.isalnum():
            return string
        else:
            num = []
            alpha=[]
            for i in range(len(s)):
                if s[i].isdigit():
                    num.append(s[i])
                elif s[i].isalpha():
                    alpha.append(s[i])

            if len(alpha) == len(num) or abs(len(num)-len(alpha))==1:
                if len(num)>len(alpha):
                    for i,j in zip(num,alpha):
                        string += i + j
                    string += num[len(num)-1]
                elif len(alpha)>len(num):
                    for i, j in zip(alpha, num):
                        string += i + j
                    string += alpha[len(alpha) - 1]
                else:
                    for i, j in zip(alpha, num):
                        string += i + j

            return string



if __name__ == '__main__':

    solution = Solution()
    print(solution.reformat("covid2019"))