class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window=0
        for i in range(k):
            window+=nums[i]
        max_sum = window
        for i in range(k, len(nums)):
            window=window-nums[i-k]+nums[i]
            max_sum=max(window, max_sum)
        return max_sum/k