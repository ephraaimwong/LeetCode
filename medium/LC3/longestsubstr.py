class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {} #(elem, index of last occurrence)
        res = 0
        leftPointer = 0
        best = 0
        for rightPointer in range(len(s)):
            if s[rightPointer] in hash and hash[s[rightPointer]] >= leftPointer: #if curr already in our window and leftPointer has not crossed over rightPointer(this occurs when there is a new window "reset" ) 
                leftPointer = hash[s[rightPointer]] + 1 #slide to the last dupe + 1
            hash[s[rightPointer]] = rightPointer #update last seen index
            currentWindow  = rightPointer - leftPointer + 1 #our current window
            best = max(best, currentWindow) #greedy update to the best seen
        return best