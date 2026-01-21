<!-- 
---
# Metadata
number: 101
name: Symmetric Tree
url: https://leetcode.com/problems/symmetric-tree/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: issymmetric_ephraim.py
    algorithm: Mirror DFS of 2 subtrees
    summary: |
      1. Recursive: Check if left subtree == right subtree from given root.
      2. Iterative: Stack of pairs.
---
-->

# Symmetric Tree
### Ephraim's solution

Before checking values, we check if DFS left and DFS right hits leafs at the same time. If depths differ, immediately we know the tree is not symmetric. If leafs are hit at the same time, we check if subtree left is identical to subtree right