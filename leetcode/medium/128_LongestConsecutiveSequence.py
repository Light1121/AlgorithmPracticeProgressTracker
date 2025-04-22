class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            cur_len = 1
            if num - 1 not in nums_set:
                current = num
                while current + 1 in nums_set:
                    current += 1
                    cur_len += 1
            ans = max(ans, cur_len)

        return ans
