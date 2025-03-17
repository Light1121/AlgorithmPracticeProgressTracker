class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        end_of_word = len(s) - 1

        while s[end_of_word] == " ":
            end_of_word -= 1

        start = 0
        for i in range(end_of_word, -1, -1):
            if s[i] == " ":
                start = i + 1
                break
            
        return end_of_word + 1 - start
