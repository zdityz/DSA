class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        k = len(nums)-1
        while i <= k:
            if nums[i]!=val:
                i+=1
            else:
                nums[i] , nums[k] = nums[k], nums[i]
                k-=1
        return k+1