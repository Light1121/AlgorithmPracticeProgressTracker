class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
The question asks for
h-index = 1 means at least 1 element has 1 or more values
h-index = 2 means at least 2 elements have 2 or more values
h-index = 3 means at least 3 elements have 3 or more values.

So sort, reverse order, and start searching for index>value.
If not, it's not valid.

The left pointer of a binary search is the last valid element.
        """
        citations.sort(reverse=True)

        length_array = len(citations)
        right = length_array
        left = 0
        while left < right:
            mid = (right+ left + 1)//2
            if citations[mid -1] >= mid:
                left = mid
            else:
                right = mid -1

        return left
