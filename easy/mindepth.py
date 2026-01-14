# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        """
        ---- Solution Intent (Deque BFS Iterative) ----
        1. Append current node.left&&right if exists
        2. Popleft deck to process next node
        
        
        i.e [rt(1), rt.left(2), rt.right(3), rt.left.left(4), rt.left.right(5), rt.right.left(6), rt.right.right(7), ...]
        
                                rt(1)
                    /                       \
                   /                         \
            rt.left(2)                       rt.right(3)
             /   \                            /     \
            /     \                          /       \
rt.left.left(4)  rt.left.right(5)   rt.right.left(6)   rt.right.right(7)
        
        
        """
        if not root: return 0
        deck = deque([(root, 1)])
        while deck:
            currentNode, depth = deck.popleft()
            
            if not currentNode.left and not currentNode.right:
                return depth
            
            if currentNode.left:
                deck.append((currentNode.left, depth + 1))

            if currentNode.right:
                deck.append((currentNode.right, depth + 1))
        