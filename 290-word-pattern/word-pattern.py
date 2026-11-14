class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split()
        dict1={}
        dict2={}
        if len(pattern) != len(words):
            return False
        for patt ,word in zip(pattern , words):
            if patt in dict1 and dict1[patt]!=word:
                return False
            if word in dict2 and dict2[word]!=patt:
                return False
            dict1[patt]=word
            dict2[word]=patt
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna