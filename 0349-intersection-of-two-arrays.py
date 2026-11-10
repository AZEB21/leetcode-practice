class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1set=set(nums1)
        num2set=set(nums2)
        inter=num1set & num2set
        return list(inter)