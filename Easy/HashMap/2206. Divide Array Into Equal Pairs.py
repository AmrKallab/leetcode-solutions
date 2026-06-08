class Solution(object):
    def divideArray(self, nums):
        freq = {}
        for i in nums :
            freq[i] = freq.get(i,0) + 1

        for  val in freq.values() :
            if val % 2 :
                return False
        return True
    
