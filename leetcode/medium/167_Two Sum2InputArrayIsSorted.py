class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) -1

        while left < right:
            ans = numbers[left] + numbers[right]
            if ans == target:
                return [left+1, right+1]
            elif ans>target:
                right -= 1
            else:
                left += 1
        