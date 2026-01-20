<!-- 
---
# Metadata
number: 21
name: Merge Two Sorted Linked Lists
url: https://leetcode.com/problems/merge-two-sorted-lists/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: mergetwosortedlinkedlists_ephraim.py
    algorithm: Two Pointer
    summary: |
      Create new head for iteration. Compare list1 and list2 current node (simultaneous walks) and zipper the order.
---
-->

# Merge Two Sorted Linked Lists
### Ephraim's solution

Create a new dummy head to track start of list to be returned. We also create an iteration node.

While we have nodes in list1 and list2 to advance, compare their values and set current.next to the smaller value. 

When either of the lists end (node = None), we just need to set append the remaining list (in its current state) to the merged list. This is possible since the lists were sorted to begin with.