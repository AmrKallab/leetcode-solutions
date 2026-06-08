class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        fre = Counter(chars)
        ans = 0

        for word in words :
            freq = fre.copy()
            check = True 
            
            for ch in word :
                if ch in freq.keys() and freq[ch] >= 1 :
                    freq[ch] -= 1
                else :
                    check = False
                    break
            if check :
                ans += len(word)
        return ans