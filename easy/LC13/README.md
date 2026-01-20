<!-- 
---
# Metadata
number: 13
name: Roman to Integer
url: https://leetcode.com/problems/roman-to-integer/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: romantointeger_ephraim.py
    algorithm: Lookahead(1) with Hashmap
    summary: |
      I<V<X<L, when current token is smaller than Lookahead(1) subtract instead of add
---
-->

# Roman To Integer
### Ephraim's solution

The <strong>Roman Numeric System</strong> already restricts input string such that cases like ```ILII``` is not possible and therefore we only need to consider valid roman numerals.

In this case, there are only 2 cases we need to consider:
1. current token < next token (i.e IV, IX)
2. current token >= next token (i.e LX, ML)

For case 1, if we subtract the current token, we get the valid output. IV = -1+5 = 4
For case 2, simply tally the tokens from left to right

We can also use a hashmap to lookup the numeric value quickly.