class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums :
            cnt = 0
            if i-1 not in nums :
                cnt += 1 
                j = i
                while j + 1 in nums :
                    j += 1
                    cnt += 1
                ans = max(ans,cnt)

        return ans
