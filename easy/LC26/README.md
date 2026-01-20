<!-- 
---
# Metadata
number: 26
name: Remove Duplicates from Sorted Array
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: removeduplicatesfromsortedarray_ephraim.py
    algorithm: Two Pointer\|Set
    summary: |
      array[:] = in-place array modification via slice notation
      1. Sets do not store duplicates
      2. Use an iterator(read) and slow pointer(write). Since read is always >= write, in-place overwriting of data is not a concern
---
-->

# Remove Duplicates from Sorted Array
### Ephraim's solution
Approach 1 (Trivial): Just add all elements into a set, convert set back to a list and in-place modify the original array with new elements.

Approach 2: Using a for loop (read pointer), check if current and next is unique. If both unique, write current element to slow pointer index. If not unique, simply advance the read pointer while slow pointer remains unchanged.

Since read index is always greater or equal to write index, we can confidently overwrite the elements of the original array in-place.