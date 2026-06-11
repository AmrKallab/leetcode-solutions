class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans , HashSet = 0 , set()
        new_idx = 0 

        for i in range(len(s)) :
            if s[i] in HashSet :

                while s[i] in HashSet :
                    HashSet.remove(s[new_idx])
                    new_idx += 1
                HashSet.add(s[i])
            else :
                HashSet.add(s[i])
            
            ans = max(len(HashSet),ans) 
        return ans 
