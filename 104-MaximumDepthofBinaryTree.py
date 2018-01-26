# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def help(self, root, num):
        if root:
            num+=1
            return max(self.help(root.left,num),self.help(root.right,num))
        return num
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num=0
        return self.help(root,num)