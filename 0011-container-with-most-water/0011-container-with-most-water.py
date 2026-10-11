class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 1
        i = 0
        j = len(height)-1
        area = 0
        while i<j:
            ans = (abs(j-i))*(min(height[j],height[i]))
            if ans>area:
                area = ans

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area