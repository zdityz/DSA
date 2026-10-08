class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        total = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            total = max(total, current)

        return total