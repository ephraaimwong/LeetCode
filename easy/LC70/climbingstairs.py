class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2: return n
        n1 = 2
        n2 = 1
        count = 0
        for i in range(3, n+1):
            count = n1+n2
            n2 = n1
            n1 = count
        return count
