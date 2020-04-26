
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.

class Solution(object):
    def minPathSum(self, grid):

        if len(grid) == 0 or grid is None:
            return 0
        dp=[[0 for i in range(len(grid))] for i in range(len(grid[0]))]

        rows = len(grid)
        col = len(grid[0])



        for i in range(rows):
            for j in range(col):
                dp[i][j] = grid[i][j]
                if i>0 and j>0:
                    dp[i][j] += min(dp[i-1][j],dp[i][j-1])
                elif i>0:
                    dp[i][j] += dp[i-1][j]
                elif j>0:
                    dp[i][j] += dp[i][j-1]

        return dp[rows-1][col-1]



if __name__ == '__main__':

    arr = [[1,3,1],[1,5,1],[4,2,1]]
    solution = Solution()
    print(solution.minPathSum(arr))