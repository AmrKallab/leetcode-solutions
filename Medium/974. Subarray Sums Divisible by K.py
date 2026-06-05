class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        curr = 0 
        cnt = 0 
        for i in nums :
            curr += i
            target = curr % k
            cnt += freq.get(target,0)
            freq[target] = freq.get(target,0) + 1 
        return cnt 