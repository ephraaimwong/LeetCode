<!-- 
---
# Metadata
number: 119
name: Pascal's Triangle II
url: https://leetcode.com/problems/pascals-triangle-ii/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: pascaltriangle2_ephraim.py
    algorithm: In-place Array Modification
    summary: |
      Append is always favored over adding to the front of array.
-->

# Pascal's Triangle II

### Ephraim's solution

1. First for loop to iterate through rows from 0 up to our target.
2. Second for loop to calculate necessary elements in current row `2nd to 2nd last elements`
    - Append row with `1` since end elements are always `1`
    - Start calculating elements `arr[n] = arr[n] + arr[n-1]`. 
        - In-place modification in this manner means that written elements is updated to current row while read elements are still values from the previous row. 
        - This method is efficient with O(1) space.
    - Alternatively, we can do a forward iteration approach by either:
        1. In-place modification; insert(0,1) then calculating middle elements; `adding to the front means the memory has to make n rightshifts`
        
        OR

        2. Using temp variable to build middle elements `easy to implement but less performant`
