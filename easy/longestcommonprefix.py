class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        --- Solution Intent (squential check) ---
        Looking only for common start characters.
        We can sort the list by word length since the max common prefix is dependent on shortest word.
        We can check the list with 1 pass by eliminating the rightmost char if no common prefix is found between words.
        This is fine since every elem in strs must have the same prefix.
        """
        if (len(strs) == 1) or (len(strs[0]) < 1):
            return strs[0]

        strs.sort(key=len) #sort list by length of elements short>>long
        #only need to check chars up to the length of the shortest word
        prefix = strs[0]

        for i in strs[1:]: #for loop from idx 1 to strs last idx
            #check if elements start with current prefix AND prefix not empty
            while not i.startswith(prefix) and prefix: 
                #if current element does not startwith prefix, try again with 1 less char
                prefix = prefix[:-1] #string slice, retain prefix from idx 0 to -1
            if not prefix: #if empty string: since bool("") == False
                prefix=""
        return prefix
        