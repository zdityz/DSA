class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window=0
        for i in range(k):
            window+=nums[i]
        
        ans = window

        for i in range(k, len(nums)):
            window = window - nums[i-k] + nums[i]
            ans = max(window,ans)
        return ans/k