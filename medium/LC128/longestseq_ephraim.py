class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ---- Solution Intent: HashSet Head-check ----
        Place all elem into a set to remove duplicates.
        Loop all elems and check if it is a HEAD. Only if HEAD, calculate the len of sequence. 
        Update longest streak with greedy approach.
        O(n) + O(n) = O(n) runtime
        """
        nums = set(nums) #O(n) run to place all in a set
        longest_streak = 0
        for elem in nums: #foreach loop can loop all elem in a set, O(n) run
            #Only runs if HEAD is encountered
            if (elem-1) not in nums: #Head of a sequence
                curr_num = elem
                curr_streak = 1
                
                while (curr_num+1) in nums: #Not the tail of current sequence
                    curr_num += 1
                    curr_streak += 1
                    
            #can also just write longest = max(curr, longest) but if's are more performant
            if curr_streak > longest_streak: 
                longest_streak = curr_streak
        return longest_streak