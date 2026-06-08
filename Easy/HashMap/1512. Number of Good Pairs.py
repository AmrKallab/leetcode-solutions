class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for i in nums :
            if i in freq :
                ans += freq[i]
                freq[i] += 1
            else :
                freq[i] += 1
        return ans