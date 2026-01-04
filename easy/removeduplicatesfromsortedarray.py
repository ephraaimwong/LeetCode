class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        --- Solution Intent 1 (Using set) ---
        add all element into a set(only unique values allowed)
        convert set to list and sort, return the list
        """
        
        myset = set()
        for i in nums:
            myset.add(i)
        nums[:] = list(myset) #reassign list for in-place data change
        nums.sort()
        return len(nums)
    
        """
        --- Solution Intent 2 (Two Pointer) ---
        loop through list, if unique is encountered assign to index tracked by a second pointer(counter)
        
        """
        if len(nums) < 1: #case where nums is empty array
            return 0
        
        result = 1 #2nd pointer
        
        for i in range(1, len(nums)): #first pointer
            current = nums[i-1]
            nxt = nums[i]
            if nxt != current: #unique pair found, do nothing if not unique
                nums[index] = nums[nxt]
                index += 1 #move pointer to where next unique should be
        
        return index
            