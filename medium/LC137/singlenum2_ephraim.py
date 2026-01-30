class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Solution Intent 1: Generic Approach to Ignore N repeated numbers 
        
        If a number is repeated N times, it will generate N number of 1 bits at specific bit string positions. If we mod N each position, we will ignore all numbers repeated N times.
        Given this logic, we can loop each bit of each number and recreate the non-repeating number as a bit string.
        
        Since python does not recognise sign bits, we need to manually implement 2's complement if resulting string spans past 31 bits.
        """
        res = 0
        N = 3
        for bit in range(32): #loop through bits from position 2^0 (LSB/rightmost) - 2^31(MSB/leftmost) but order does not matter in this case since we only care about the 1's 
            count = 0 #count number of 1's
            for num in nums: #O(n) runtime
                if (num>>bit) & 1: #bit rightshift to the "current" bit being evalulated. & 1(...0001 in binary) which tells us if evaluated bit is 1 (1&1 == 1(true)), then enter loop, if bit is 0 (0&1 == 0(false))
                    count += 1
            if count % N != 0: #repeated numbers will produce N number of 1's, if mod n != 0 then we have found the bit for a number that is not repeated by N times (unique or target number)
                res = res | 1 << bit # 1<<bit left shifts bit to correct position i.e. 1 to 001000. The bitwise or (|) acts as a merger, 1 | 1 = 1; 0|1 = 1; 0|0 = 0. It preserves 1's of previous result iterator.
        if res >= 2**31: res -= 2**32 #res is an unsigned bit string currently ie. 111110101, python does not use recognise sign bits, therefore we need to manually 2's complement the result bit string if it takes up all 32 positions (0's get dropped). If 32 positions are used it is either the edge case of this logic(do not consider since max value for this qns is 2^31 -1) or a negative number
        return res
        """
        ---- Solution Intent 2: K-Map
        
        treat this appearOnce and appearTwice as a running tally of numbers within them.
        
        if num is part of the tally within appearOnce, that number is zero'ed out (subtracted) from the tally.
        
        numbers should trickle from state 00 to 01 to 10 to being removed from our evaluation circuit
        """
        appearOnce = 0 #state 01
        appearTwice = 0 #state 10
        for num in nums: #new numbers are state 00
            #once bitwise op is called, we are only working in bit strings
            appearOnce ^= num & ~appearTwice #if num is part of appearOnce (commutative property of bitwise XOR and AND) appearOnce will == ...000
            appearTwice ^= num & ~appearOnce # & ~ used together essentially creates a rejection gate that sets string to ...000 if is encountered. 
        return appearOnce