class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = set()
        for i in range(n):
            hashset = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    ans.add(triplet)
                hashset.add(nums[j])
        return [list(triplet) for triplet in ans]
