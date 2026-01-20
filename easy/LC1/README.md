<!--
---
# Metadata
number: 1
name: Two Sum
url: https://leetcode.com/problems/two-sum/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: twosum_ephraim.py
    algorithm: Hashmap of Visited
    summary: |
      {VisitedNumber: Its_Index}
      Scans array and determine if complement exists within a single pass.
---
-->

# Two Sum
### Ephraim's solution
1. Loop through the numbers array
2. Calculate the complement to current value
3. Check if complement number was already visited
4. If not, add current number to the hashmap with {currentNumber: current_index}

### Runtime: O(n)
