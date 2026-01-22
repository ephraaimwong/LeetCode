class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        ---- Solution Intent 1: Two Sum ----
        Requires all levels to be built.
        """
        res = [[1]]
        if numRows == 1: #base case
            return res 
        for level in range(1, numRows):
            currArr = [1] #build array for each level. Will always start with 1
            for i in range(1, level): #elements that need to be calculated 2nd to 2nd last
                tally = res[level-1][i-1] + res[level-1][i] #grab elements from previous level
                currArr.append(tally)
            currArr.append(1) #will always end with 1
            res.append(currArr)
        return res
    
        """
        ---- Solution Intent 2: Hockey Stick O(n^3) Bad Solution----
        Requires a 3rd for loop to get sum of all elements of same index from start to target level
        """
        res = [[1]]
        if numRows == 1: return res
        for level in range(1, numRows):
            currArr = [1]
            for i in range(1, level):
                hockeystick = 0
                for column in range(i-1, level):
                    hockeystick += res[column][i-1]
                currArr.append(hockeystick)
            currArr.append(1)
            res.append(currArr)
        return res