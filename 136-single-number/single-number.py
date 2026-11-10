class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        num_dict={}
        for num in nums:
            num_dict[num]=num_dict.get(num ,0)+1
        for num in nums:
            if num_dict[num]==1:
                return num


            
             