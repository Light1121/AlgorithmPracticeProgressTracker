class Solution(object):
    def removeElement(self, nums, num):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        #my attempt,  ALSO 100%
        # use index and end pointer, 
        # check if index = num
        # if it is the look right to left using end
        # end untill they meet
        """
        index = 0      # Pointer moving from left to right
        end = len(nums) - 1  # Pointer moving from right to left

        while index <= end:  # Stop when the two pointers meet
            if nums[index] == num:
                while index < end and nums[end] == num:  # Find the first non-'num' element from the right
                    end -= 1
                nums[index], nums[end] = nums[end], nums[index]  # Swap elements
                end -= 1  # Move 'end' pointer left
            index += 1  # Move 'index' pointer right
        
        return end + 1  # New length of the array
        """

        #this is the solution
        index = 0 
        for i in nums:
            if i != num:
                nums[index] = i
                index += 1
        return index

