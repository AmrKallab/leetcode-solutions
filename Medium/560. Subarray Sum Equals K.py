class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        cnt = 0 
        curr = 0 
        for i in nums :
            curr += i 
            if curr - k in freq :
                cnt += freq[curr-k]
            freq = freq.get(curr,0) + 1 
        return cnt