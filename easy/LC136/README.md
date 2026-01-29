<!-- 
---
# Metadata
number: 136
name: Single Number
url: https://leetcode.com/problems/single-number/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: singlenum_ephraim.py
    algorithm: XOR bit manipulation
    summary: |
      a XOR a == 0
---
-->

# Single Number
### Ephraim's solution

The question constraints solutions to O(n) run and O(1) space. This means that we can only store a single variable to get the non-repeated elem.

Luckily, elem XOR elem == 0 and this property is commutative (order does not matter). 
```
4 XOR 1 XOR 4 XOR 1 == 0

4 XOR 1 XOR 4 == 1
```
Therefore, it all elements are double repeated but for one, XOR all elem will leave the non-repeated (in binary) XOR 0 which is the non-repeated elem.