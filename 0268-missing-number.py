class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        my_set=set(nums)
       
        for num in range(len(nums)+1):
            if num not in my_set:
                return num