class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums :
            freq[i] += 1
        ans = 0 
        for val in freq.values() :
            if val == 1 :
                return -1 
            if val % 3 == 0 :
                ans += val // 3
            else :
                ans += val // 3 + 1
        return ans
