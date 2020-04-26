
# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1

class BinaryMatrix(object):

   def get(self, x, y):
      # mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
       mat = [[0,0],[0,1]]
       return mat[x][y]


   def dimensions(self):
       #mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
       mat = [[0,0],[0,1]]
       return [len(mat),len(mat[0])]


class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        dim = binaryMatrix.dimensions()
        i = 0
        j = dim[1]-1
        finalIndex = j
        isIndex = False

        while i<dim[0] and j>=0:

            if binaryMatrix.get(i,j) == 1:
                isIndex = True
                finalIndex = min(finalIndex,j)
                j -= 1
            else:
                i += 1
        if not isIndex:
            return -1
        else:
            return finalIndex





if __name__ == '__main__':

    solution = Solution()
    binary = BinaryMatrix()
    print(solution.leftMostColumnWithOne(binary))


