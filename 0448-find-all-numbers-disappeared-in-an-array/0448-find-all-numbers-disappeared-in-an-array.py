class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i) - 1
            if nums[index]>0:
                nums[index] = -nums[index]
        ans = []

        for j in range(len(nums)):
            if nums[j]>0:
                ans.append(j+1)
        return ans