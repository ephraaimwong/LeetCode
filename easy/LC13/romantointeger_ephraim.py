class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100,
            'D':500,
            'M':1000
        }
        # --- Solution Intent 1 (if I or X or C precedes) ---
        # if encounter I/X/C, lookahead 1
        # if condition met, result -= I/X/C instead of adding it
        # tally the roman numbers
        # this works since IV = 4 when I is encountered result -= 1 then V is encountered result += 5, result delta = -1 + 5 = 4
        result = 0
        for i in range(len(s)):
            if i < (len(s)-1): #len(s)-1 prevents out of index error due to lookahead 1
                if s[i] == 'I':
                    if s[i+1] == 'V' or s[i+1] == 'X':
                        result -= values[s[i]]
                        continue
                if s[i] == 'X':
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        result -= values[s[i]]
                        continue
                if s[i] == 'C':
                    if s[i+1] == 'D' or s[i+1] == 'M' :
                        result -= values[s[i]]
                        continue

            result += values[s[i]]
            print(result)
        
        # --- Solution Intent 2 (no switch cases) ---
        # roman numbers already have rules where I can only be before V and X, X can only be before L and C ,...
        # observation 1: cases like ICX will never appear
        # observation 2: I<V & X; X<L&C ; C<D&M
        #so if lookahead value > current value, minus current
        #else tally all current values
        
        for i in range(len(s)):
            if i < (len(s)-1) and values[s[i+1]] > values[s[i]]: #len(s)-1 prevents out of index error due to lookahead 1
                result -= values[s[i]]
                continue
            result += values[s[i]]
        return result
                    