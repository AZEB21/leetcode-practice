class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=right=0
        limit=len(nums)
        while right<limit:
            if nums[right]!=0:
                numbers=nums[left]
                nums[left]=nums[right]
                nums[right]=numbers
                left+=1
            right+=1
               
           