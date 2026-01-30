<!--
---
# Metadata
number: 137
name: Single Number II
url: https://leetcode.com/problems/single-number-ii/

# List of Collaborator Solutions
solutions:
  - author: Ephraim
    language: python
    filename: singlenum2_ephraim.py
    algorithm: Bit count by column
    summary: |
      Given a target and current value, building a complement hashmap
      allows us to scan array and determine if complement exists within a single pass.    
---
-->


# Single Number II
### Ephraim's solution
#### Approach 1: Generic algo to ignore numbers repeated N times
If number is repeated N times, it will generate N number of 1 bits at specific positions. 
```
i.e. 5 = 101
if 5 appears twice in the array, it will contribute 2 1bits to position 0 and 2

if 5 appears 4 times, it will contribute 4 1 bits to position 0 and 2
```
We can see that this property holds true even when different numbers are thrown into the mix. 
```
i.e 9 = 1001
```
Therefore if we tally the number of 1's from all numbers at each bit position (column by column), tally % N will give us the 1 bit of specific columns of the non-repeating number.

To properly implement this logic, we have an outer loop of bit positions and an inner loop of every number in the array.

##### Part 1: Reading 
Within this inner loop, we shall do a bitshift to the current column and extract the rightmost bit via `&1` (bitwise AND). 
```
i.e. num = 1101101; column = 4
num >> 4 = 0000110
0000110 & 1 is 0000110 & 0000001 which is 0000000
Masking Property Leveraged:
0 & 0 = 0 
0 & 1 = 0
1 & 1 = 1
General Formula for rightmost bit extraction:
number & 2^(N)-1
i.e 
1 bit = number & 2^1 - 1
2 bit = number & 2^2 - 1
3 bit = number & 2^3 - 1
```
##### Part 2: Writing
After reading the non-repeating bit, we write it in the appropriate column position.
```
1 << column left shifts the bit to the correct column.
i.e if column is 7
1 << 7 is 00000001 shifted to 10000000
```
This shifted bit string is then merged with current result via `result |` (bitwise OR).
```
i.e. result = 1110001010001
result = resullt | (1 << 7)
1110001010001 | 10000000 which is
11100*1*1010001

Preservation Property Leveraged:
0 | 0 = 0
1 | 0 = 1
1 | 1 = 1

As long as a 1 been previously written, it will be preserved in all future iterations.
** Note that since we are building the result column by column, we do not need to consider cases where a bit should be a 1 when it is a 0.
```
##### Part 3: Python specific
Python does not recognise signed bits, therefore we need to manually implement 2's complement on the result bit string if it takes up 31 bits (question constrains numbers to 2^31 - 1).
```
111....0101 is basically a negative number but python treats it as a positive

edge case of 1111...1111 (2^31) does not need to be considered due to the question constrain.

2's Complement: if negative number, just subtract a bitstring of all 1's i.e. 2^32
2^32 because it is the difference between +2^31 and -2^31; 2^31 - (-2^31) = 2*2^31 = 2^32
General Formula: Inverting bit numbers
Where K is the sign bit (MSB), 2's complement = 2^(K+1)
```

#### Approach 2: K-Map using Rejection Gates
Refer to [LC136](/easy/LC136/singlenum_ephraim.py) for how bitwise XOR works.

As stated above, `&` has masking properties which can be used in conjection with `~ (bitwise NOT)` to create rejection gates (set difference)

```
i.e. 
If I want to reject 9(1001) from the running tally(1101), 1101 & ~1001 is 1101 & 0110 -> 0100 (4).

This is basically a conditional minus or A/B set difference "A - A ∩ B"
```
For every number, we check if it is first encounter (number does not get zeroed during XOR appearOnce and is not gatekept by appearTwice's tally).

If it does not survive that check (does not go into appearOnce's tally), it is not a first appearance BUT will be removed from its tally. We then check if it is a 2nd or 3rd appearance. If num is not gatekept by appearOnce's tally, twos grabs the number. If nums appears a 3rd time, appearTwice will remove it from the tally, effectively dropping the number from evaluation.

**State 01 takes priority to grab numbers, if state 01 does not claim a number, state 10 will then claim it.