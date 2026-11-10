class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_magazine={}
        for char in magazine:
            dict_magazine[char]=dict_magazine.get(char,0)+1
        for char in ransomNote:
            if dict_magazine.get(char,0)==0:
              return False

            dict_magazine[char] -=1
        return True 
    
