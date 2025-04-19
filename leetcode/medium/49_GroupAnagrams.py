class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # it store the sorted string as KEY
        # array of string  that has same sorted string as VALUE
        the_map = {}

        # Loop strs
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # sort the string check if is in the map
            if sorted_word not in the_map:
                    # if its not --> add and append
                    the_map[sorted_word] = []
            # if its in --> append
            the_map[sorted_word].append(word)

        
        return list(the_map.values())
