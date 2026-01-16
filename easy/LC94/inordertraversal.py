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
        #1 recursion
        def dfs(visits, node):
            if not node: #current node is None (when leaf node.left||node.right is called)
                return
            dfs(visits, node.left) #keep calling left to the stack
            visits.append(node.val) #add current node.val (basically root for every subtree)
            dfs(visits, node.right) #keep calling right to stack

        result = []
        dfs(result, root)
        
    
        #2 stack iteration
        stack = []
        result = []
        currentNode = root
        #for a valid tree, the root will be the bottom of the stack
        while currentNode or len(stack)>0: #when len(stack) == 0 there is no more parent node from starting position (i.e. DFS left finished, popped root but DFS right not completed). Therefore, we need to check that currentNode exists
            while currentNode: #DFS left
                stack.append(currentNode)
                currentNode = currentNode.left
            currentNode = stack.pop()
            result.append(currentNode.val) #root for tree/subtree
            currentNode = currentNode.right #go right and triggers the DFS left above
            
        #3 Morris Traversal Algorithm
        result = [] 
        curr = root 
        while curr: 
            if not curr.left: 
                result.append(curr.val) 
                curr = curr.right 
            else: 
                predecessor = curr.left 
                
                # Loop to find the predecessor
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right 
                
                # Link/Unlink Logic
                if not predecessor.right:
                    predecessor.right = curr 
                    curr = curr.left 
                else: 
                    predecessor.right = None 
                    result.append(curr.val)
                    curr = curr.right 
                
        return result
    
        #4 recursive the template
        """
        Not recommended. List concatention is expensive compared to appending to a list
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) #call stack DFS left then list concatentate [root.val] to root node before DFS to right in the same way
