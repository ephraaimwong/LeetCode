# Instructions
<strong>Do not change the table of content's format before prior approval. </strong>
### New Problem Process
1. Link the LeetCode Problem Description ```[Name of Problem](URL)```
2. Create a new folder ```LC<problem_number>```
3. Edit readme to link folder in step 2 ```[LC<problem_number>](difficulty/LC<problem_number>)```
4. Commit solution to the new folder
### Existing Problem Process
1. Find the existing solution sub-folder. <em>It should be linked in the readme.</em>
2. Commit solution
3. Update repo readme [language, key concept, algorithm]   

# Easy
| LeetCode #| Language | Solution  |Algorithm/Approach|<div style= "width:150px;">Key Concept(s) </div>|
| - | - | - | - | - |
| [1 - Two Sum](https://leetcode.com/problems/two-sum/description/https:/) | python | [LC1](easy/LC1) |Hashmap Complement|Given a target and current value, building a complement hashmap allows us to scan array and determine complement in a single pass|
|[9 - Palindrome Number](https://leetcode.com/problems/palindrome-number/)|python|[LC9](easy/LC9)|Reverse String \| Mod(10) digit by digit reversal | mod(10), integer division 10 will remove rightmost digit, add digit and *10 for every digit will place digit in correct position|
|[13 - Roman To Integer](https://leetcode.com/problems/roman-to-integer/description/)|python|[LC13](easy/LC13/romantointeger.py)|Lookahead(1) with hashmap|Rules built into the roman system constrain numbers to allow I<V<X<L... therefore if a smaller number appears before bigger number, it is prefix and you subtract prefixes|
|[14 - Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)|python|[LC14](easy/LC14)|Sort By Length, Constrain search to shortest word|Prefix MUST appear in all elements to be valid, use all letters in shortest word and loop the array, eliminate rightmost char if not valid till empty or valid|
|[20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|python|[LC20](easy/LC20)| Stack with Hashmap Complements| Push bracket complements onto the stack when encountered, pop from stack when char matches. Return not empty |
|[21 - Merge Two Sorted Linked Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)|python|[LC21](easy/LC21)|Zipper Approach|Current a new head and node for iteration. Compare list1 and list2 current node value and set the walk accordingly.|
|[26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)|python|[LC26](easy/LC26)|Set \| Two Pointer|1: Sets will ignore duplicates <br>2: Use iterator (read) and slow pointer (write), since read is faster than write, overwriting data is not a concern|
|[27 - Remove Element](https://leetcode.com/problems/remove-element/description/)|python|[LC27](easy/LC27)|Two Pointer|Use iterator (read) and slow pointer (write), since read is faster than write, overwriting data is not a concern|
|[28 - Find index of first occurrence in a string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)|python| [LC28](easy/LC28)|||
|[35 - Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)|python|[LC35](easy/LC35)|Binary Search|Binary Search is O(log N). <br>On crossover, upper is the floor (number rounded-down/last smaller number) and lower is the ceiling(number rounded up/next biggernumber)|
|[58 - Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/)|python|[LC58](easy/LC58)|Strip,Split|Strip removes leading and trailing whitespace, split breaks string into array|
|[66 - Plus One](https://leetcode.com/problems/plus-one/description/)|python|[LC66](easy/LC66)||1. Digit by digit extraction<br>2. Implement a carry for char == 9|
|[67 - Add Binary](https://leetcode.com/problems/add-binary/description/)|python|[LC67](easy/LC67)|typecast, binary cast|int(string,base) tells computer that string is in form of base x NOT convert string to base x.|
|[69 - Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)|python|[LC69](easy/LC69)|Binary Search|Use range 0 - x (sqrt(x) cannot be bigger than x), return upper since we want the floor(number rounded down)|
|[83 - Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)|python|[LC83](easy/LC83)|Singly Linked List| Nodes are already sorted, if currentNode == nextNode, set current.next to 2 ahead and kill the next node (killNode = None). Only advance when current != next|
|[70 - Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)|python|[LC70](easy/LC70)|gotta revisit|ways(N) = ways(N-1) + ways(N-2) <br>|
|[88 - Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)|python|[LC88](easy/LC88)|3 Pointer|Direction of pointers are dependent on overwriting ability when carrying out in-place sorting|
|[94 - Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)|python|[LC94](easy/LC94)|DFS|1. Recursive, call left till None, then right till none <br>2. Stack: when len(stack) == 0, there is no parent above current. Check if there is a parent and current exists(allows loop to continue when switching from root to DFS right). <br> DFS left while pushing all nodes into stack, whenever no more left, try right which should loop DFS left again if available|
|[108 - Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)|python|[LC108](easy/LC108)|Binary Search DFS|Instead of discarding elements as with a search, we use middle partitioning to separate left and right elements from a given point to create height balanced tree|
|[104 - Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)|python|[LC104](easy/LC104)|DFS with count|Return an incremented count in recursive DFS|
|[101 - Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)|python|[LC101](easy/LC101)|Mirror DFS of 2 subtrees|<strong>Stack = DFS; Queue = BFS</strong><br>Check if current leftTree == current rightTree whilst doing a parallel walk.<br>1. Recursive MirrorTree<br>2. Iterative Stack of Pairs |
|[111 - Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)|python|[LC111](easy/LC111)|BFS|BFS use deque. <br>1. Append left && right if they exist. <br>2. Popleft to process current<br>Terminate Search at the first leaf to get min depth.|
||||||
# Medium
| LeetCode #| Language | Solution |Algorithm/Approach|<div style= "width:150px;">Key Concept(s) </div>|
| - | - | - | - | - |
<!-- START Medium -->
|[2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|python|[LC2](medium/LC2)|Linked List, Integer Division, Modulo|Read value, calculate sum, update carry, repeat till l1 and l2 and carry is finished|
||||||
<!-- END Medium -->