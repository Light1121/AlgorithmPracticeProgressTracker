class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s_to_t = {}  # s → t
        map_t_to_s = {}  # t → s

        for i, s_letter in enumerate(s):
            t_letter = t[i]

            if s_letter in map_s_to_t and map_s_to_t[s_letter] != t_letter:
                return False

            if t_letter in map_t_to_s and map_t_to_s[t_letter] != s_letter:
                return False
            map_s_to_t[s_letter] = t_letter
            map_t_to_s[t_letter] = s_letter
        
        return True