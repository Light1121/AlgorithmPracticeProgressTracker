"""
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #method 1：
        # convert the int to string then compare last ditgite to first
        #until goes to mid

        # # negative number has to be wrong
        # if x < 0:
        #     return False
        
        # # to string and put it into list
        # x_str = list(str(x))
        
        # # comapre the last digit with first
        # # loop sokeep going to mind
        # left, right = 0, len(x_str) - 1
        # while left < right:
        #     if x_str[left] != x_str[right]:
        #         return False
        #     left += 1
        #     right -= 1
        
        # return True

        ##########################################
        #method 2
        # almost the same as first, but just invert the whole int
        # by using sliders [::-1]
        # compare only once

        if x < 0:
            return False
        return str(x) == str(x)[::-1]