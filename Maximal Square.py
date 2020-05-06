
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return
        area = 0
        sol = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        for i in range(len(matrix)):
            sol[i][0] = int(matrix[i][0])
            if sol[i][0] == 1:
                area = 1
        for i in range(1,len(matrix[0])):
            sol[0][i] = int(matrix[0][i])
            if sol[0][1] == 1:
                area = 1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '1':
                    sol[i][j] = min(int(sol[i][j-1]),int(sol[i-1][j]),int(sol[i-1][j-1]))+1
                    area = max(sol[i][j],area)
                else:
                    sol[i][j] = 0
        return area * area



if __name__ == '__main__':
    arr = [["0","0"],["0","1"]]
    solution = Solution()
    print(solution.maximalSquare(arr))