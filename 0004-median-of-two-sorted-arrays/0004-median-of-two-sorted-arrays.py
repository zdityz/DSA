class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)

        if n % 2 == 1:
            return nums[n // 2]
        else:
            a = nums[n // 2]
            b = nums[(n // 2) - 1]
            return (a + b) / 2