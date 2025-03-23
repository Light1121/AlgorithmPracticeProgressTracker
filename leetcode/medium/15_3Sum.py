class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for fix_num in range(len(nums) -2): # at least 3 number
            if fix_num > 0 and nums[fix_num] == nums[fix_num-1]: # avoid duplicated
                continue
            #init the low high value
            low = fix_num + 1
            high = len(nums) - 1

            # inner loop for getting right combination
            while low < high: 
                total = nums[fix_num] + nums[low] + nums[high]

                if total == 0:
                    ans.append([nums[fix_num], nums[low], nums[high]])
                    low += 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1 
                elif total < 0:
                    low += 1
                else:
                    high -= 1
        
        return ans