class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        the_map = {}

        for char in magazine:
            if char not in the_map:
                the_map[char] = 1
            else:
                the_map[char] += 1
            
        for char in ransomNote:
            if char not in the_map or the_map[char] == 0 :
                return False
            else:
                the_map[char] -= 1
        
        return True