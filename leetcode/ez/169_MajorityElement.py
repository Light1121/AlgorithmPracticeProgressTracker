#this is so ez, 
# just sort, 
# then the cluster will definitly over the mid point.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]