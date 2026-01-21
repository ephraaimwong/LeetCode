<!-- 
---
# Metadata
number: 88
name: Merge Sorted Array
url: https://leetcode.com/problems/merge-sorted-array/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: mergesortedarray_ephraim.py
    algorithm: 3 Pointer
    summary: |
      Direction of pointers are dependent on overwriting ability when carrying out in-place sorting
      There are dummy elements at the later half of target array, hence we write from the back instead of the front.
---
-->

# Remove Duplicates from Sorted List
### Ephraim's solution
The target array already has dummy elements accounting for the number of elements of list2.

We can read from the back of the last valid element in both list and have a slow writing pointer at the end of the target array. Since both reads are ahead of the write pointer, overwriting is not a concern.