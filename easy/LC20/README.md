<!-- 
---
# Metadata
number: 20
name: Valid Parentheses
url: https://leetcode.com/problems/valid-parentheses/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: validparentheses_ephraim.py
    algorithm: Stack of Complements
    summary: |
      Push bracket complements onto the stack when encountered, pop from stack when char matches. Return not empty
---
-->

# Valid Parentheses

### Ephraim's solution

Using hashmap, we can push brackets to the stack as we encounter them if they are opening bracket. ```i.e ([{```

We can then peek the stack's complement and pop if it matches.

```
i.e. 
stack = ["(", "[" ]
input = "])"
         ^
```
If `]`'s complement is stack.peek(), then we pop the stack.

The stack should be empty at the end since every opening bracket will have the correct closing bracket IN ORDER.
If stack is not empty at the end, either there are missing pair(s) OR there is errorenous pattern(s).
