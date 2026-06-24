class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict = {}
        for i in range(len(nums2)) :
            
            while stack and nums2[stack[-1]] < nums2[i] :
                dict[nums2[stack[-1]]] = nums2[i]  
                
                stack.pop()
            stack.append(i)

        res = []

        for i in nums1 :
            if i in dict.keys() :
                res.append(dict[i])
            else :
                res.append(-1)
        return res