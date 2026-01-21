<!-- 
---
# Metadata
number: 69
name: Sqrt(x)
url: https://leetcode.com/problems/sqrtx/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: addbinary_ephraim.py
    algorithm: Binary Search
    summary: |
      Use range(0 - x) since sqrt(x) cannot be greater than x.
      Return upper since we are looking for the floor (rounded-down).
---
-->

# Sqrt(x)
### Ephraim's solution
Refer to [LC35](../LC35/README.md) for explanation on binary search.

We can employ the binary search algorithm where mid*mid == x as the target. We will eventually find either the sqrt(x) = mid or a crossover will occur. In the latter, we return upper since the question asks for a rounded-down number.