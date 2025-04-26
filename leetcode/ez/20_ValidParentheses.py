class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        pairs = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        stack = []
        for string in s:
            if string in '({[':
                stack.append(string)
            else:
                if not stack or stack[-1] != pairs[string]:
                    return False
                stack.pop()
        return not stack