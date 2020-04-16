# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if self.left == None and self.right == None:
            return 0
        
        return max(self.diameterOfBinaryTree(self.left), self.diameterOfBinaryTree(self.right)) + 1