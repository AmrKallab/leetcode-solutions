class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [nums[0]] * len(nums)
        rightsum = [nums[-1]] * len(nums)
        for i in range(1,len(nums)) :
            leftsum[i] = leftsum[i-1] + nums[i]

        for i in range(len(nums)-2,-1,-1) :
            rightsum[i] = rightsum[i+1] + nums[i]

        res = []
        for i in range(len(nums)) :
            res.append(abs(leftsum[i] - rightsum[i]))
        return res
    
