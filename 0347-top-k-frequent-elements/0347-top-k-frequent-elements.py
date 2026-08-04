class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i in nums:
            seen[i] = seen.get(i,0)+1
        ans = sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]
        return [i for i, freq in ans]