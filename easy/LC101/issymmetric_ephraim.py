# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        """
        ---- Solution Intent 1 (Recursive DFS) ----
        Compare DFS left to DFS right and vice versa between 2 trees
        
                                  rt
                        /                   \
                 rt1                         rt2
              /      \                    /      \
        rt1.left    rt1.right       rt2.left    rt2.right
        """
        if not root: return True
        #check if 2 trees are mirrors given their roots
        def mirrorTree(root1, root2): 
            if not root1 and root2: #hit leaf nodes at same time
                return True
            elif not root1 or root2: #only 1 tree hit leaf node
                return False
            else:
                # call mirror for DFS left on 1 tree, DFS right on other tree, repeat for opposite sides 
                return root1.val == root2.val and mirrorTree(root1.left, root2.right) and mirrorTree(root1.right, root2.left)
        return mirrorTree(root.left, root.right)
    
        """
        ---- Solution Intent 2 (Iterative Stack of Pairs) ----
        TLDR; Stack = DFS; Queue = BFS
        Parallel walking of trees
        """
        if not root: return True
        stack = [(root.left, root.right)] # push pairs
        while stack: #while there are not parents above starting pair
            left, right = stack.pop()

            if not left and not right: #both trees hit leaf tgt
                continue
            elif not left or not right or left.val != right.val: #only 1 hit leaf or current node.val on left != right
                return False

            #appending mirroring nodes at each depth level
            stack.append((left.left, right.right))
            stack.append((right.left, left.right))

        return True