class Solution:
    def maxArea(self, height: list[int]) -> int:
        result=0
        # for line in range (len(height)):
        #     container =height[line]* line
        #     if container >result:
        #         result=container 
        left=0
        right=len(height)-1
        while left<right:
            width=right-left
            area=width * min(height[right],height[left])
            if area>result:
                result=area
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
        return result