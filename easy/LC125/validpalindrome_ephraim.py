class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        ---- Solution Intent 1: Two Pointer O(1) memory ----
        While forward and backward iterators do not cross over, simply compare chars, if the string manages not to throw false after pointers meet, it is a palindrome.
        
        Simply move pointer if char is not alphanumeric
        """
        left = 0
        right = len(s)-1
        while left < right: #did not crossover 
            while left < right and not s[left].isalnum(): #enforce crossover and shift pointer till alphanumeric is found 
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower(): #many lower() calls but perserves O(1) mem
                return False
            left += 1
            right -= 1
        return True

        """
        ---- Solution Intent 2: Two Pointer O(n) memory ----
        Same as solution 1 but normalize the string before comparison.
        Use a stringbuilder approach
        """
        s = s.lower()
        left = 0
        right = len(s)-1
        s = "".join(ch for ch in s if ch.isalnum()) #oneliner immediately hands join() the char, eliminating the need for temporary/intermediate variables
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
        """
        ---- Solution Intent 3: Regex Sub ----
        Sub all NOT alphanumeric char to empty
         
        """
        # [] - character set to match
        # [^...] - negate the regex search
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        
        #creates a new reversed string, reverse() is in-place modification and cannot be used for immutable (strings, tuples, etc...)
        return s == s[::-1] 