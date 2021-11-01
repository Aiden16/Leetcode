class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1=0
        p2=len(height)-1
        area=0
        while p1<=p2:
            area=max(area,min(height[p1],height[p2])*(p2-p1))
            if height[p1]>height[p2]:
                p2-=1
            else:
                p1+=1
        return area
            # area=max(area,height[p1]*height[p2])
            # if height[p1]>height[p2]: