<!-- 
---
# Metadata
number: 108
name: Convert Sorted Array to Binary Search Tree
url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: heightbalancedBST_ephraim.py
    algorithm: Binary Search Depth First Build
    summary: |
      Use Binary Search Partioning where root.left = lowerhalf mid, root.right = upperhalf mid

---
-->

# Minimum Depth of Binary Tree
### Ephraim's solution
Call the binary search partitioning recursively to depth first build a tree. 

While crossover does not occur, Root.left = mid where the array shrinks into its lower half. Root.right = mid where array shrinks into its upper half.  