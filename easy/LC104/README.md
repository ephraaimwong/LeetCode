<!-- 
---
# Metadata
number: 104
name: Maximum Depth of Binary Tree
url: https://leetcode.com/problems/symmetric-tree/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: maxdepth_ephraim.py
    algorithm: DFS with count return
    summary: |
      DFS with incremented count return
---
-->

# Maximum Depth of Binary Tree
### Ephraim's solution
Bottom up counting.

DFS to leaf and start counting depth on return. Return max count recursively to preserve highscore as you DFS the tree.