class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        the_map= {}

        # loop s count each char num of time occcure
        for char in s:
            if char in the_map:
                the_map[char] += 1
            else: 
                the_map[char] = 1


        # loop t, each char check exsit in map or not
        for char in t:
            if char not in the_map:
                # if not just false
                return False
            elif the_map[char] == 0:
                return False
            else:
                the_map[char] -= 1

        # finished looping meaning able to build
        return True