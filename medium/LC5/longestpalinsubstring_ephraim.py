class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        ---- Solution Intent: Widest Width/Centric Expansion ----
        Treat every char as a potential center and explore the max valid palindrome substring from that point.
        Need to compare even and odd possible palindromes.
        """
        def expand_from_center(string, center_left, center_right):
            while center_left >= 0 and center_right < len(string) and string[center_left]==string[center_right]:
                center_left -= 1
                center_right += 1
            return center_left + 1, center_right-1 #this is returned as a tuple

        longest = [0,0]
        for i in range(len(s)):
            #odd and even are tuples
            odd = expand_from_center(s, i, i) #odd palindromes have a center, therefore left and right pointers are init to the same
            even = expand_from_center(s, i, i+1)# even palindromes do not have center, either left or right pointer must be offset by 1
            curr = max(odd, even, key=lambda x: x[1] - x[0]) #lambda function to compare the difference of start,end between odd and even 
            if (curr[1]-curr[0]) > (longest[1]-longest[0]):
                longest = curr #greedy update
        return s[longest[0]:longest[1]+1]#python slice end is exclusive, our end index is inclusive.
