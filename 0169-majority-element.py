class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        seen= {}
        for i in range(len(nums)):
            seen[nums[i]]=seen.get(nums[i],0)+1
        majority=len(nums)//2
        for j in seen:
           if seen[j]>majority:
              return j