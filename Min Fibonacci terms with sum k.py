
class Solution(object):
    def findMinFibonacciNumbers(self, k):
        fiboList = [0,1,1]
        if k == 0:
            return 0
        elif k==1 or k==2:
            return 2
        count = 0
        i=3
        next = 1

        while next <= k:
            next = fiboList[i-1]+fiboList[i-2]
            fiboList.append(next)
            i += 1
        fiboList.pop()
        j = len(fiboList)-1

        while k>0:
            count += k//fiboList[j]
            k %= fiboList[j]
            j -= 1
        return count




if __name__ == '__main__':

    solution = Solution()
    print(solution.findMinFibonacciNumbers(19))