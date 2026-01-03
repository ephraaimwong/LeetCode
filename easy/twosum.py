class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # --- Solution Intent ---
        # loop through nums array
        # find complement value for current number
        # check if complement value has been visited
        # if not found, store current number as key with its index as value in hashmap
        # return [] if nothing is found
        
        numsHash = {}

        for i in range(len(nums)):
            pairValue = target - nums[i] # find the value required from current number in nums
            if pairValue in numsHash:
                return [i, numsHash[pairValue]] 
            numsHash[nums[i]] = i # (key,value) = (number, index_in_nums)

        return []