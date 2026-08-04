<!--
---
# Metadata
number: 3 
name: Longest Substring Without Repeating Characters
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: longestsubstr.py
    algorithm: Sliding Window
    summary: |
      Hash map to store the "last seen" index of current elem.
      Slide leftpointer to last duplicate + 1 when current elem has already appeared in this window.
---
-->


# Longest Substring Without Repeating Characters
### Ephraim's solution
We use a hash map to store the last seen index of the current element. Using a 2 pointer approach, we can create a sliding window and evaluate all valid substrings in a single pass using O(n) time.

When the current element has already been encountered within the current window (ie. a*e*bcd**e**), we slide the left pointer to the right of the older duplicated (i.e a**b**bcde). Therefore, we can evaluate all slices of valid windows as we traverse the string.

We then calculate the length of the current window at the end of each loop and only update when a better length has been found. This method will ensure that all valid windows (including all subsets of a larger window) will be evaluated.
