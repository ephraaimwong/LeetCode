<!-- 
---
# Metadata
number: 83
name: Remove Duplicates from Sorted List
url: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: removeduplicatesfromsortedlist_ephraim.py
    algorithm: Singly Linked List Traversal
    summary: |
      Delete nodes by setting to None(null)
      If current == next, set current to 2 ahead (current.next.next). Kill skipped nodes.
---
-->

# Remove Duplicates from Sorted List
### Ephraim's solution
Since the list is already sorted, we can simply walk the list and comparing current to next. If current == next, set current to 2 ahead (current.next.next). We check again and only allow the walk to advance when current != next.