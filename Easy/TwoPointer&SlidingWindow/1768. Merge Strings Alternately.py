class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr = 0
        word = []
        while ptr < len(word1) or ptr < len(word2) :
            if ptr < len(word1) :
                word.append(word1[ptr])
            if ptr < len(word2) :
                word.append(word2[ptr])
            ptr += 1
       
        return ''.join(word)
        