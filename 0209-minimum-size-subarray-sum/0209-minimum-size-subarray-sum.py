class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        wind = 0
        ans = float('inf')
        for right in range(len(nums)):
            wind+=nums[right]
            while wind>=target:
                ans = min(ans, right - left + 1)
                wind-=nums[left]
                left+=1
        return 0 if ans == float('inf') else ans