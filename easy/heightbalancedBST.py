# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        """
        ---- Solution Intent 1 (Pointer) ----
        using binary search's partitioning algorithm, build node with DFS instead of discarding !targets
        """
        def build(nums, lower, upper):
            if lower > upper: #cross over occurs (1 level below level )
                return None
            mid = (lower + upper) // 2
            root = TreeNode(nums[mid]) #set mid as root for current subtree
            root.left = build(nums, lower, mid-1) #recursive DFS left to build
            root.right = build(nums, mid+1, upper) #recursive DFS right to build
            return root
        return build(nums, 0, len(nums)-1)
    
        """
        ---- Solution Intent 2 (Array Slicing) ----
        does not require helper function BUT array slicing is inefficient for time(big big diff) and memory, pointer is favored
        """
    
        def sortedArrayToBST(self, nums):
            """
            :type nums: List[int]
            :rtype: Optional[TreeNode]
            """
            if len(nums) == 0:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root    