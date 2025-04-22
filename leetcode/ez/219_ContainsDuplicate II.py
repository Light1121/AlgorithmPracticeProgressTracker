class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        the_map = {}
        for i in range(len(nums)):
            if nums[i] in the_map and (i - the_map[nums[i]]) <= k:
                return True
            else:
                the_map[nums[i]] = i
        return False