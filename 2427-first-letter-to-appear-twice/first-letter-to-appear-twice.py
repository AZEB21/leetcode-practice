class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # string_set=set(s)
        my_dict={}
        for ch in s:
            my_dict[ch]=my_dict.get(ch,0)+1
            if my_dict.get(ch,0)==2:
                return ch
               


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna