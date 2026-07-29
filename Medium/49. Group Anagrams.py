class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hash = defaultdict(list) 

        for stri in strs :
            key = ''.join(sorted(stri))
            Hash[key].append(stri)

        return list(Hash.values())