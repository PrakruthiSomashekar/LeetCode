class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):

        if root is None:
            return 0

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)

        return max(lheight + rheight, max(ldiameter,rdiameter))

    def height(self,root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left),self.height(root.right))


if __name__ == '__main__':
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    child4 = TreeNode(5)

    root.left = child1
    root.right = child2
    child1.left = child3
    child1.right = child4
    solution = Solution()
    print(solution.diameterOfBinaryTree(root))