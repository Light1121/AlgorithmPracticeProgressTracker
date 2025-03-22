class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, ((right - left) * min(height[left],height[right])))

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area