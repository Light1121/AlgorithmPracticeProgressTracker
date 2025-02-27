class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: # if there nothing in num2 then
            return nums1 # num1 is already sort
        
        # the first m element are from array1 and the rest s 0
        # change all the 0 into numbers from array 2
        nums1[m::] = nums2[::]
        nums1.sort() # remain sorted