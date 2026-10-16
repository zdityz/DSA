class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        wind = 0
        for i in range(k):
            wind+=arr[i]
        
        if wind >= (threshold*k):
                count+=1

        for i in range(k, len(arr)):
            wind = wind - arr[i-k] + arr[i]
            if wind >= (threshold*k):
                count+=1
        
        return count