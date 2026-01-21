<!-- 
---
# Metadata
number: 94
name: Binary Tree Inorder Traversal
url: https://leetcode.com/problems/binary-tree-inorder-traversal/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: inordertraversal_ephraim.py
    algorithm: DFS
    summary: |
      For trees, when len(stack) = 0, there are no parent nodes above it. To ensure loops continue switching from left to right, you ADDITIONALLY need to check for currentNode != None. 
      1. Recursive: Call left till None, then right till None
      2. Stack: Push left nodes if as long as valid, then pop and push right
---
-->

# Binary Tree Inorder Traversal
### Ephraim's solution
Approach 1: Trivial

Approach 2: While node is valid, push left. Pop and push right(resets left depth push). 