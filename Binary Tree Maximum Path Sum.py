# Given a non-empty binary tree, find the maximum path sum

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.maximum = float('-inf')
        def dfs(root):
            if root is None:
                return 0
            leftMax = max(0,dfs(root.left))
            rightMax = max(0,dfs(root.right))
            self.maximum = max(self.maximum, leftMax+rightMax+root.val)
            return max(leftMax,rightMax)+root.val
        dfs(root)
        return self.maximum



if __name__ == '__main__':
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)

    root.left = child1
    root.right = child2
    solution = Solution()
    print(solution.maxPathSum(root))