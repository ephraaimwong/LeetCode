<!-- 
---
# Metadata
number: 118
name: Pascal's Triangle
url: https://leetcode.com/problems/pascals-triangle/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: pascaltriangle_ephraim.py
    algorithm: Two Sum
    summary: |
      1. Double for loop: 1 for levels, 1 for calculating elements
      2. Hockey Stick: Element n, level m is sum of all elements n-1 from levels n-1 to m-1
---
-->

# Pascal's Triangle
### Ephraim's solution
Approach 1: We can use a double for loop, 1 for levels and 1 for calculating elements for current level.

We can sequentially build the triangle level by level using the two sum approach of index-1 and index of previous level from elements from 2nd to 2nd last in the current level.

Approach 2: BAD but fun

The Hockey stick concept shows that element n, level m is the sum of all n-1 elements from level n-1 to m-1
        
    level  0         '1
           1       '1   *1
           2     '1   *2   1
           3   '1   *3   3   1
           4 1   ='4   =*6   4   1
i.e 4 is index 1 of level 4 which is index 0 of levels (1-1) to (5-1) or 1+1+1+1

Requires a 3rd for loop to sum the hockey stick.
