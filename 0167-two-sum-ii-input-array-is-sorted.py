class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        while right>left:
         total =numbers[left]+numbers[right]
         if target ==total:
           return [left +1 ,right+1]
         elif total<target:
             left+=1
         else:
            right-=1

        