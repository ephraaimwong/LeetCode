class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        """
        --- Solution Intent ---
        Use substring match and find()
        """
        
        index = -1

        if needle in haystack:
            index = haystack.find(needle)
        return index
        