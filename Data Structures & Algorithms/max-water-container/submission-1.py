class Solution:
    def maxArea(self, heights: list[int]) -> int:
        areas=[]
        for i in range (len(heights)-1):
            for j in range(i+1, len(heights)):
                area=(j-i)*(min(heights[i], heights[j]))
                areas.append(area)
        return max(areas)