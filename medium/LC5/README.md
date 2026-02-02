<!-- 
---
# Metadata
number: 5
name: Longest Palindromic Substring
url: https://leetcode.com/problems/longest-palindromic-substring/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: longestpalinsubstring_ephraim.py
    algorithm: Centric Expansion
    summary: |
      Expand Around Center is specialized 2 Pointer to find widest width of a certain pattern(symmetry, etc...).
      Start from a center and expand whilst property is valid.
      Treat each char as a potential center point use greedy approach to update longest substring.
---
-->

# Longest Palindromic Substring
### Ephraim's solution

Exapnd Around Center is a specialized 2 pointer approach starts from a center and expand outwards while pattern/property is valid to find the widest width that is still valid. In this case, since odd and even palindromes requires different center points, it is better to have a left_of_center and right_of_center pointers where odd starts at the same index whilst even has 1 pointer offset.

In the helper function, we expand until start and end indices are invalid, therefore we need to return indices 1 step before invalid (left + 1, right - 1).

In the main loop, we treat every char as a potential center point and greedy update for the longest valid palindromic substring. 