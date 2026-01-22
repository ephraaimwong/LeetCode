class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
        ---- Solution Intent 1: In-place Two Sum ----
        We only need to return target row. We can just build and overwrite array till we obtain the target row.
        """
        res = [1]
        if rowIndex == 0:
            return res

        for row in range(rowIndex):
            res.append(1) #last elem is always "1"
            for i in range(len(res)-2, 0, -1): #2nd last elem to 2nd elem
                res[i] = res[i]+res[i-1]

        return res