<!-- 
---
# Metadata
number: 35
name: Search Insert Position
url: https://leetcode.com/problems/search-insert-position/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: searchinsertposition_ephraim.py
    algorithm: Binary Search
    summary: |
      Binary Search Runtime is O(log n).
      On crossover, upper is the floor (last smaller number/rounded-down) while lower is the ceiling (next bigger number/ rounded-up)
---
-->

# Search Insert Position
### Ephraim's solution

Binary Search requires a sorted array.

We start with upper = largest element and lower = smallest element.
Steps:
1. While crossover does not occur (upper >= lower), calculate the middle. 
2. If middle is target, return it. 
3. If target is greater than middle, we raise the lower to middle + 1.
4. If target is less than middle, we reduce upper to middle - 1.

If crossover occurs and target is not found, we have reached the position where the target should/would be if it existed. Upper will represent the number rounded-down `i.e. number = 2.9123; upper = 2`
Lower will represent the number rounded-up `i.e. number = 2.9123; lower = 3`