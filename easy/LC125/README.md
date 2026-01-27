<!-- 
---
# Metadata
number: 125
name: Valid Palindrome
url: https://leetcode.com/problems/valid-palindrome/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: validpalindrome_ephraim.py
    algorithm: 2 Pointer
    summary: |
      .alnum() checks if char is alphanumeric
      variable[::-1] is string reversal
      1. In-place search without normalizing data  - O(1) Mem O(n) Run
      2. Search after normalization with string building - O(n) Mem O(n) Run
      3. Regex "Blacklist" Substitution

---
-->

# Valid Palindrome
### Ephraim's solution
#### 2 Pointer
Left and right pointer, move it towards opposing ends until crossover occurs. If at any point char at left != chat at right, invalid palindrome is detected. We dont need to think about left and right movement synchronization since a valid palindrome will always meet in the middle(even) or 1 before center (odd). In either scenario, as long as the shortcircuit is not triggered, the palindrome is still valid. 

Approach 1 (Most performant): By parsing the string without normalizing, no extra temp/intermediary variables are required. O(1) memory

#### Normalization
Normalization requires a string building approach that requires memory for every char parsed to be stored, evaluated and passed.

Approach 2 (2 pointer): Normalize the string by building from an empty string joined with char where char is .alnum()

Approach 3 (Regex Sub): Create a blacklist to normalize the string [^a-zA-Z0-9] where ^ refers to negation of the character set.