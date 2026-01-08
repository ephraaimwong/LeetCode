class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        ---- Solution Intent (Binary Search) ----
        using range 0 - x, do midPoint ** 2.
        if result > x, midPoint is too big (set as new upper)
        if result < x, midPoint is too small (set new lower)
        return upper since we want the floor (rounded down number) if crossover happens
        """
        upper = x
        lower = 0
        midPoint = (upper - lower) // 2
        while upper >= lower:
            res = midPoint*midPoint
            if res == x:
                return midPoint
            elif res > x:
                upper = midPoint - 1
                midPoint = (upper - lower) // 2
            else:
                lower = midPoint + 1
                midPoint = lower + (upper + lower) // 2
        return upper 
         