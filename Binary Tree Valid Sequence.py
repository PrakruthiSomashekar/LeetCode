
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidSequence(self, root, arr):
        if root is None:
            return False
        return self.isValid(root,arr,0)

    def isValid(self,node, arr, index):
        if node.val != arr[index]:
            return False
        if index == len(arr)-1:
            return node.left==None and node.right==None
        if node.left!=None and self.isValid(node.left,arr,index+1):
            return True
        if node.right!=None and self.isValid(node.right,arr,index+1):
            return True
        return False

if __name__ == '__main__':
    root = TreeNode(0)
    c1 = TreeNode(1)
    c2 = TreeNode(0)
    c3 = TreeNode(0)
    c4 = TreeNode(1)
    c5 = TreeNode(0)
    root.left = c1
    root.right = c2
    c1.left = c3
    c1.right = c4
    c2.left = c5
    arr = [0,1,0]
    solution = Solution()
    print(solution.isValidSequence(root,arr))