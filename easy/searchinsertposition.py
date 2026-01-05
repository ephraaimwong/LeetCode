class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
        ---- Solution Intent (Binary Search) ----
        O(log n) runtime specified which is binary search
        """
        upper = len(nums) - 1
        lower = 0
        midPoint = (upper - lower) // 2
        # >= means that upper and lower will cross over (1 step after upper == lower) This is necessary to prove that target does not exist in the array. If DNE, upper will give index of last smallest number before target. Lower will give index of first bigger number before target.  
        while upper >= lower:
            if nums[midPoint] == target: return midPoint
            elif target > nums[midPoint]:
                lower = midPoint + 1
                midPoint = lower + (upper - lower) // 2
            else:
                upper = midPoint - 1
                midPoint = (upper - lower) // 2
        return lower #we want to insert the index of first bigger number 

        

        
