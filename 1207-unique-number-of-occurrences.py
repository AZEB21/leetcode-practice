class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        my_dict={}
        for num in arr:
            my_dict[num]=my_dict.get(num ,0)+1
        freq=list(my_dict.values())
        return len(freq)==len(set(freq))
