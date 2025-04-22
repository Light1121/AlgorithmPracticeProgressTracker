class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        the_set = set()
        while n not in the_set:
            the_set.add(n)
            ttl = 0
            while n:
                ones=(n%10)**2
                ttl+=ones
                n=n//10
            n = ttl
            if n == 1:
                return True
        return False