# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 #already at leaf
        left = self.maxDepth(root.left) #recursive DFS to left
        right = self.maxDepth(root.right) #recursive DFS right
        return 1 + max(left, right) # will constantly add 1 for every level and return the max height for left, right subtree for every recursive call