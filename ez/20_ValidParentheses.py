class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_set = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for char in s:
            if char in valid_set:  # if left Parentheses
                stack.append(char)
            else:  # if right Parentheses
                if not stack or valid_set[stack[-1]] != char:
                    # does not match
                    return False
                stack.pop() # pop if matched
        #when there is nothing in stack meaning it work
        return len(stack) == 0