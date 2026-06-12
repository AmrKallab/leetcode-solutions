from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False 

        window1 = Counter(s1)
        window2 = Counter(s2[:len(s1)])

        if window1 == window2 :
            return True

        for i in range(len(s1),len(s2)) :

            window2[s2[i-len(s1)]] -= 1

            window2[s2[i]] += 1

            if window2[s2[i-len(s1)]] == 0 :
                del window2[s2[i-len(s1)]]

            if window1 == window2 :
                return True 

        return False 