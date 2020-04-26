
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):

        if len(grid) == 0:
            return 0
        numberOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numberOfIslands += self.dfs(i, j, grid)

        return numberOfIslands

    def dfs(self, i, j, grid):
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0'):
            return 0

        grid[i][j] = '0'
        self.dfs(i+1,j,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i,j+1,grid)
        self.dfs(i,j-1,grid)
        return 1


if __name__ == '__main__':

    arr = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
   # arr = [['1'],['1']]
    solution = Solution()
    print(solution.numIslands(arr))