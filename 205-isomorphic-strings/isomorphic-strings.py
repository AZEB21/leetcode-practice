class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for char1, char2 in zip(s, t):
            if char1 in dict1 and dict1[char1] != char2:
                return False

            if char2 in dict2 and dict2[char2] != char1:
                return False

            dict1[char1] = char2
            dict2[char2] = char1

        return True