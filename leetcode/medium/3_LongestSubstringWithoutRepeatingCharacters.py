class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        # left right pointer
        # left: when there is repeated
        # right: when there si no repeated
        left, right = 0, 0
        max_length = 0
        seen = {} #char : index

        # for loop to the entire string, only move right pointe
        # mean while keep track on max length by right - left + 1
        for right in range(len(s)):
            #if right pointe's element in seen
            # update the left pointer to the seen element +1 index
            # also updates the seens index
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            #else make right pointer element to seen with its index
            seen[s[right]] = right
            #updated length
            max_length = max(max_length, right - left + 1)
            
        
        #return outcome
        return max_length