class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) <= 1:
            return path

        result_stack = []
        path = path.split('/')
        for filename in path:
            if filename == "..":
                if result_stack:
                    result_stack.pop()
            elif filename == "." or filename == "":
                continue
            else:
                result_stack.append(filename)
        
        return '/' + '/'.join(result_stack)