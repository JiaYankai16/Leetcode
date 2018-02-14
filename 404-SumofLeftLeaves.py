# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def help(self,root,sum):
        if root.left:
            if root.left.left==None and root.left.right==None:
                sum+=root.left.val
            sum=self.help(root.left,sum)
        if root.right:
            sum=self.help(root.right,sum)
        return sum
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        sum=0
        return self.help(root,sum)