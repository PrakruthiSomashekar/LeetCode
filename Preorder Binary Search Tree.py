
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):

    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root


    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)



if __name__ == '__main__':
    arr = [4,2]
    solution = Solution()
    solution.inorder(solution.bstFromPreorder(arr))