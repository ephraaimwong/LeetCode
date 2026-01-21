<!-- 
---
# Metadata
number: 111
name: Minimum Depth of Binary Tree
url: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: mindepth_ephraim.py
    algorithm: BFS with depth count
    summary: |
      BFS uses deque([]), append current's child and popleft to process nodes in depth order.

---
-->

# Minimum Depth of Binary Tree
### Ephraim's solution
With a BFS, the first leaf node hit is the shortest height or min depth of the tree.

By using tuple pairs of (node , depth), we can track nodes and their respective depths. popleft() to process the nodes by level. We check if current node is a leaf (does not have left or right). If not a leaf, we append its children to the deque.
