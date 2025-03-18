class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if  numRows ==1: return s

        cycle = 2 * (numRows - 1)
        result = []

        for j in range(0, len(s), cycle):
            result.append(s[j])

        for i in range(1, numRows - 1):
            for j in range(i, len(s), cycle):
                result.append(s[j])
                diag = j + cycle - 2 * i
                if diag < len(s):
                    result.append(s[diag])

        for j in range(numRows - 1, len(s), cycle):
            result.append(s[j])

        return "".join(result)