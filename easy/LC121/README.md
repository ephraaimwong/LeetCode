<!-- 
---
# Metadata
number: 121
name: Best Time to Buy and Sell Stock
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: buystocks_ephraim.py
    algorithm: Greedy Algorithm
    summary: |
      Buy and sell must be in respect to time, we cannot use a 2 pointer approach.
      Greedy approach makes the best locally available choice(respects the time constraint)
---
-->

# Best Time to Buy and Sell Stock
### Ephraim's solution
Greedy Approach: 
1. Update lowest price if new low is encountered. 
2. Calculate current profit from current low

This approach next evaluates best choice moving forward. Also this is a `single pass solution`!

We can also implement a 2 pointer (sliding window) approach as long as we ensure buy pointer (slow) is behind sell pointer (current item).

