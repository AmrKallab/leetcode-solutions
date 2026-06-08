class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        has_odd = False
        for key , val in counter.items() :
            if val % 2 == 0 :
                res += val 
            else :
                res += val - 1
                has_odd = True

        if has_odd :
            return res + 1
        return res