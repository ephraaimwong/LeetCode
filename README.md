<details open> 
    <summary> <h1>Instructions</h1> </summary>

<strong>Do not change the table of content's format before prior approval. </strong>

1. Create new branch from main `LC<problem_number>_author`.
    - Pull main regularly if you open a branch for more than a single day
    - Don't bother trying to push to main directly (`protected branch hook declined` error will be thrown)

<details> <summary><h3>New Problem Process Steps 2 - 4</h3></summary>

2. Create a new folder ```LC<problem_number>``` under the appropriate difficulty folder ```easy, medium, hard```
3. Clone [template_README.md](templates/template_README.md) and rename to README.md
4. Fill out the YAML frontmatter as directed in the template and include the README.md in the corresponding folder in step 2.
</details>
<details> <summary><h3>Existing Problem Process Steps 2 - 4</h3></summary>

2. Find the existing solution folder ```LC<problem_number>```. <em>It should be linked in the readme.</em>
3. Commit solution to the folder.
4. Update the README.md within solution folder ```i.e. easy/LC1/README.md```, follow the [template](templates/template_README.md) for how to add additional contributor(s) and solution(s) to existing problems.
</details>

(...continued)

5. Commit solution as ```filename_authorname``` to folder in step 2.
    - Use a sensible commit message `i.e LC83`, gibberish will be rejected in the pursuit of sanity maintenance.

6. Pull Request to main and wait for approval.
</details>   

<details> <summary><h1>Easy</h1></summary>

<!-- START Easy -->
| LeetCode #| Language | Solution |Algorithm/Approach|<div style= "width:150px;">Key Concept(s) </div>|
| --- | --- | --- | --- | --- |
|[1 - Two Sum](https://leetcode.com/problems/two-sum/)|python|[LC1](easy/LC1/twosum_ephraim.py)|Hashmap of Visited|{VisitedNumber: Its_Index}<br>Scans array and determine if complement exists within a single pass.|
|[9 - Palindrome Number](https://leetcode.com/problems/palindrome-number/)|python|[LC9](easy/LC9/palindromenumber_ephraim.py)|Rightmost Digit Manipulation|%10 extracts rightmost digit<br>//10 removes rightmost digit|
|[13 - Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|python|[LC13](easy/LC13/romantointeger_ephraim.py)|Lookahead(1) with Hashmap|I<V<X<L, when current token is smaller than Lookahead(1) subtract instead of add|
|[14 - Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|python|[LC14](easy/LC14/longestcommonprefix_ephraim.py)|Search by GCD|Constrain search space to GCD(shortest word)|
|[20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|python|[LC20](easy/LC20/validparentheses_ephraim.py)|Stack of Complements|Push bracket complements onto the stack when encountered, pop from stack when char matches. Return not empty|
|[21 - Merge Two Sorted Linked Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|python|[LC21](easy/LC21/mergetwosortedlinkedlists_ephraim.py)|Two Pointer|Create new head for iteration. Compare list1 and list2 current node (simultaneous walks) and zipper the order.|
|[26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|python|[LC26](easy/LC26/removeduplicatesfromsortedarray_ephraim.py)|Two Pointer\|Set|array[:] = in-place array modification via slice notation<br>1. Sets do not store duplicates<br>2. Use an iterator(read) and slow pointer(write). Since read is always >= write, in-place overwriting of data is not a concern|
|[27 - Remove Element](https://leetcode.com/problems/remove-element/)|python|[LC27](easy/LC27/removeelement_ephraim.py)|Two Pointer|In python: <br>for i in range() >> regular for loop<br>for i in items >> foreach loop<br>Use iterator (read) and slow pointer (write), since read is faster than write, overwriting data is not a concern.|
|[28 - Find index of first occurrence in a string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)|python|[LC28](easy/LC28/firstoccurrence_ephraim.py)|None||
|[35 - Search Insert Position](https://leetcode.com/problems/search-insert-position/)|python|[LC35](easy/LC35/searchinsertposition_ephraim.py)|Binary Search|Binary Search Runtime is O(log n).<br>On crossover, upper is the floor (last smaller number/rounded-down) while lower is the ceiling (next bigger number/ rounded-up)|
|[58 - Length of Last Word](https://leetcode.com/problems/length-of-last-word/)|python|[LC58](easy/LC58/lengthoflastword_ephraim.py)|Text Processing|strip() removes leading and trailing whitespace<br>split() breaks string into array elements|
|[66 - Plus One](https://leetcode.com/problems/plus-one/)|python|[LC66](easy/LC66/plusone_ephraim.py)|Loop Shortcircuit|1. Rightmost digit extraction (mod 10)<br>2. Loop from back and only carry if leftmost is 0|
|[67 - Add Binary](https://leetcode.com/problems/add-binary/)|python|[LC67](easy/LC67/addbinary_ephraim.py)|Binary Casting|int(string,base) tells computer that string is in form of base x NOT convert string to base x.|
|[69 - Sqrt(x)](https://leetcode.com/problems/sqrtx/)|python|[LC69](easy/LC69/addbinary_ephraim.py)|Binary Search|Use range(0 - x) since sqrt(x) cannot be greater than x.<br>Return upper since we are looking for the floor (rounded-down).|
|[83 - Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|python|[LC83](easy/LC83/removeduplicatesfromsortedlist_ephraim.py)|Singly Linked List Traversal|Delete nodes by setting to None(null)<br>If current == next, set current to 2 ahead (current.next.next). Kill skipped nodes.|
|[88 - Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|python|[LC88](easy/LC88/mergesortedarray_ephraim.py)|3 Pointer|Direction of pointers are dependent on overwriting ability when carrying out in-place sorting<br>There are dummy elements at the later half of target array, hence we write from the back instead of the front.|
|[94 - Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|python|[LC94](easy/LC94/inordertraversal_ephraim.py)|DFS|For trees, when len(stack) = 0, there are no parent nodes above it. To ensure loops continue switching from left to right, you ADDITIONALLY need to check for currentNode != None. <br>1. Recursive: Call left till None, then right till None<br>2. Stack: Push left nodes if as long as valid, then pop and push right|
|[101 - Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|python|[LC101](easy/LC101/issymmetric_ephraim.py)|Mirror DFS of 2 subtrees|1. Recursive: Check if left subtree == right subtree from given root.<br>2. Iterative: Stack of pairs.|
|[104 - Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|python|[LC104](easy/LC104/maxdepth_ephraim.py)|DFS with count return|DFS with incremented count return|
|[108 - Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)|python|[LC108](easy/LC108/heightbalancedBST_ephraim.py)|Binary Search Depth First Build|Use Binary Search Partioning where root.left = lowerhalf mid, root.right = upperhalf mid|
|[111 - Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|python|[LC111](easy/LC111/mindepth_ephraim.py)|BFS with depth count|BFS uses deque([]), append current's child and popleft to process nodes in depth order.|
|[118 - Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)|python|[LC118](easy/LC118/pascaltriangle_ephraim.py)|Two Sum|1. Double for loop: 1 for levels, 1 for calculating elements<br>2. Hockey Stick: Element n, level m is sum of all elements n-1 from levels n-1 to m-1|
|[121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|python|[LC121](easy/LC121/buystocks_ephraim.py)|Greedy Algorithm|Buy and sell must be in respect to time, we cannot use a 2 pointer approach.<br>Greedy approach makes the best locally available choice(respects the time constraint)|
|[125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|python|[LC125](easy/LC125/validpalindrome_ephraim.py)|2 Pointer|.alnum() checks if char is alphanumeric<br>variable[::-1] is string reversal<br>1. In-place search without normalizing data  - O(1) Mem O(n) Run<br>2. Search after normalization with string building - O(n) Mem O(n) Run<br>3. Regex "Blacklist" Substitution|
<!-- END Easy -->
</details>
<br>

<details> <summary><h1> Medium</h1></summary>

<!-- START Medium -->
| LeetCode #| Language | Solution |Algorithm/Approach|<div style= "width:150px;">Key Concept(s) </div>|
| --- | --- | --- | --- | --- |
|[2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|python|[LC2](medium/LC2/addtwo.py)|Hashmap Complement|Given a target and current value, building a complement hashmap<br>allows us to scan array and determine if complement exists within a single pass.|
|[128 - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|python|[LC128](medium/LC128/longestseq_ephraim.py)|Hashset Head-check|foreach loop iterates sets<br>Sequences DO NOT need to be in-order<br>Calculate the length of sequences when a HEAD is encountered|
<!-- END Medium -->
</details>
<br>
<details> 
    <summary><h1> Hard</h1></summary>

<!-- START Hard -->
| LeetCode #| Language | Solution |Algorithm/Approach|<div style= "width:150px;">Key Concept(s) </div>|
| --- | --- | --- | --- | --- |
<!-- END Hard -->
</details>
