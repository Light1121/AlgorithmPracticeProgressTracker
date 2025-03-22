class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        current_index = 0
        for char in t:
            if char == s[current_index]:
                current_index += 1
            if current_index == len(s):
                return True
        return False