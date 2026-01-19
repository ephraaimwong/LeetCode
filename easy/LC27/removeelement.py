class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        """
        --- Solution Intent (Two Pointer) ---
        Write and advance slow pointer when !target
        """
        
        pointer =0
        for i in range(len(nums)): # i is treated as index counter
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
                
        # for i in nums: #this is foreach instead
        #     if i != val:
        #         nums[pointer] = i
        #         pointer += 1

        return pointer