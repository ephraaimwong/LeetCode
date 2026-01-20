<!-- 
---
# Metadata
number: 14
name: Longest Common Prefix
url: https://leetcode.com/problems/longest-common-prefix/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: longestcommonprefix_ephraim.py
    algorithm: Search by GCD
    summary: |
      Constrain search space to GCD(shortest word) 
---
-->

# Longest Common Prefix
### Ephraim's solution

Since prefix is greatest common denominator, we can start with the shortest word and search down the list, removing the rightmost char if match is not found.