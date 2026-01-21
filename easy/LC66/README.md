<!-- 
---
# Metadata
number: 66
name: Plus One
url: https://leetcode.com/problems/plus-one/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: plusone_ephraim.py
    algorithm: Loop Shortcircuit
    summary: |
      1. Rightmost digit extraction (mod 10)
      2. Loop from back and only carry if leftmost is 0
---
-->

# Plus One
### Ephraim's solution
Approach 1: Use rightmost digit extraction with mod 10 and add to an int with 10**power.

Approach 2: Loop from the back. If current digit is < 9, we increment. If current digit is 9, when set to 0. If leftmost digit is 0, we employ list concatenation to add a carry. If all digits are <9, we can shortcircuit to skip the list concatenation. 

This approach works since we are only adding a grand total of 1, therefore `999+1 = 1000`. There is only 1 potentially cascading carry to deal with.