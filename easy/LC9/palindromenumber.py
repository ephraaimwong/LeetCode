class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # --- Solution Intent 1 (using string casting) ---
        # string cast x and store a reversed x
        # check if x is the same sequence as reversed x
        
        if x < 0:
            return False
        
        x= str(x)
        reversedX = x[::-1] #reversing string

        if x == reversedX: return True
        return False
        
        # --- Solution Intent 2 (reversing int sequence) ---
        # x mod 10 = last digit  (ie 13344331 % 10 = 1)
        # store that last digit as first digit in reversed sequence
        # reversed * 10 (this will bump the current reversed sequence to the left by 1) + last digit 
        # check if x == reversed
        # We know that negative cannot be palindrome
        # numbers ending with 0 cannot be palindrome either (ie. 0334330 is 334330 as int)
        
        if x < 0 | x % 10 == 0 & x!= 0:
            return False

        temp = x    
        reversedX = 0

        while temp > 0:
            rightmostDigit = temp % 10
            temp //= 10 #integer division deletes right most digit in the sequence (ie 1234//10 = 123)
            reversedX *= 10 
            reversedX += rightmostDigit

        if x == reversedX: return True
        return False

