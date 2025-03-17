"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # ending position index
        end_index = len(nums) - 1

        # start the loop at ONE BEFORE ending
        # until reached the ending index again
        for i in range(len(nums)-2, -1, -1):
            # each time if the range are cover the end
            if i + nums[i] >= end_index:
                #update the new ending (meaning reachable)
                end_index = i
        
        #if it end up at the first index 0 meaning there is path
        return True if end_index == 0 else False