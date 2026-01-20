<!-- 
---
# Metadata
number: 27
name: Remove Element
url: https://leetcode.com/problems/remove-element/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: removeelement_ephraim.py
    algorithm: Two Pointer
    summary: |
      In python: 
      for i in range() >> regular for loop
      for i in items >> foreach loop
      Use iterator (read) and slow pointer (write), since read is faster than write, overwriting data is not a concern.
---
-->

# Remove Duplicates from Sorted Array
### Ephraim's solution
Using a for loop (read pointer), check if current is target. If not target, write current element to slow pointer index. If target, simply advance the read pointer while slow pointer remains unchanged.

Since read index is always greater or equal to write index, we can confidently overwrite the elements of the original array in-place.