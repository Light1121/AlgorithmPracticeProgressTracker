class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ### binary search are always left prio ###
        ### since // 2 will round down so left ###

        right = len(nums) - 1
        left = 0

        while left <= right: #must use left first
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid  - 1
        return left # must return left
        