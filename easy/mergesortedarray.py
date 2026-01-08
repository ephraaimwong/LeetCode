class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        ---- Solution Intent (Overwrite in-place in reverse) ----
        since the back of nums1 is padded with arbitrary zeros, we can overwrite from the back without worries.
        given nums1 and nums2 are sorted, we can use 3 pointers (1 for looping nums1, nums2 and merge position in reverse).
        since mergePointer is the farthest back (slowest pointer), we are essentially reading ahead of the write position.
        """
        
        num1Pointer = m - 1
        num2Pointer = n - 1
        mergePointer = len(nums1) - 1
        while num2Pointer >= 0: #there is elem in nums2 to merge
            #check if there is elem within m sequence to merge
            if num1Pointer >=0 and nums1[num1Pointer] > nums2[num2Pointer]: 
                nums1[mergePointer] = nums1[num1Pointer]
                num1Pointer -= 1
            else:
                nums1[mergePointer] = nums2[num2Pointer]
                num2Pointer -= 1
            mergePointer -= 1