<!--
---
# Metadata
number: 128 
name: Longest Consecutive Sequence
url: https://leetcode.com/problems/longest-consecutive-sequence/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: longestseq_ephraim.py
    algorithm: Hashset Head-check
    summary: |
      foreach loop iterates sets
      Sequences DO NOT need to be in-order
      Calculate the length of sequences when a HEAD is encountered 
---
-->


# Longest Consecutive Sequence
### Ephraim's solution
Since sets do not allow duplicates, we can ignore cases of double counting elements. 

A sequence HEAD is where there is no valid previous element, in this case number-1 DNE in the set.

When we encounter a HEAD, we walk all consective numbers while TAIL is not encountered (element + 1 exists in set).

Since this algorithm only triggers on HEAD elements, we dont need to consider cases all other NON-HEAD elements `i.e. [1,2,3,4,5] algorithm only calculates streak from '1', DOES NOT calculate streak from '2','3', etc...`

Greedy update the longest streak and return it at the end.