class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
            
        output = []
        low = 0
        for high in range(1, len(nums)):
            if nums[high] != nums[high - 1] + 1:
                if low == high - 1:
                    output.append(str(nums[low]))
                else:
                    output.append(str(nums[low]) + "->" + str(nums[high - 1]))
                low = high
        if low == len(nums) - 1:
            output.append(str(nums[low]))
        else:
            output.append(str(nums[low]) + "->" + str(nums[-1]))

        return output



            
