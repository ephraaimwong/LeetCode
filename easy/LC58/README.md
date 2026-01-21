<!-- 
---
# Metadata
number: 58
name: Length of Last Word
url: https://leetcode.com/problems/length-of-last-word/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: lengthoflastword_ephraim.py
    algorithm: Text Processing
    summary: |
      strip() removes leading and trailing whitespace
      split() breaks string into array elements
---
-->

# Length of Last Word
### Ephraim's solution

Remove leading and trailing whitespace with strip() and then split the string into array elements with split(" ").

Simply return the length of the last array element.