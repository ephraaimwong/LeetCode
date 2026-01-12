# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        #DSF left, root, right
        
        def dfs(visits, node):
            if not node: #current node is None (when leaf node.left||node.right is called)
                return
            dfs(visits, node.left) #keep calling left to the stack
            visits.append(node.val) #add current node.val (basically root for every subtree)
            dfs(visits, node.right) #keep calling right to stack

        result = []
        dfs(result, root)
        return result