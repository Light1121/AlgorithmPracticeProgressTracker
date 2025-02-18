"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        1.  do (target number) - (current number in the list) = subtracted number
        2. see if the subtracted number is in the list or not. 
        3. IF its not then save it in the dictionary, we might find the matching pair in the future.
        """

        
        # hash table
        #make a dict, each pair is like (subtracted number : position index)
        subValue_index = {}

        #loop each element
        for i in range(len(nums)):
            subtracted_num = target - nums[i]
            # if the matching pair is found (adds up to target)
            if nums[i] in subValue_index:
                # then thats the answer
                return [i, subValue_index[nums[i]]]
            #else then save it for later, might exsit in further
            subValue_index[subtracted_num] = i
