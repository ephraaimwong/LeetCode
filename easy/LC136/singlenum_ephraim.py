class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ---- Solution Intent: XOR ----
        Since constraits are O(n) run and O(1) space, XOR bit manipulation is best.
        
        elem XOR elem = 0
        if there is only 1 non-repeated elem with all else repeated twice, XOR all elem will cancel out all double repeated.
        """
        
        result = 0
        for i in nums:
            result ^= i
        return result