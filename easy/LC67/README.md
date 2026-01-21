<!-- 
---
# Metadata
number: 67
name: Add Binary
url: https://leetcode.com/problems/add-binary/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: addbinary_ephraim.py
    algorithm: Binary Casting
    summary: |
      int(string,base) tells computer that string is in form of base x NOT convert string to base x.
---
-->

# Add Binary
### Ephraim's solution
Since we are given 2 binary strings, we can typecast it from string to an int using int(string, 2) which tells the computer to convert the string that is a number in base 2 into an integer of base 10.

We can add the two int and cast it back to a binary string using bin().