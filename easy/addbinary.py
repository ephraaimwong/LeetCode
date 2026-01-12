class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2) #tells computer that a is string number of base 2
        b = int(b,2) #will convert to integer base 10
        res = a+b
        return bin(res)[2:] #binary string will start with 0b 