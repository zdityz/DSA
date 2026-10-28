class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = 0
        end = len(nums)-1
        left = -1
        right = -1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                left=mid
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                right=mid
                start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return [left,right]