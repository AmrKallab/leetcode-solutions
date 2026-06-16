class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == len(set(nums)) :
            return False 

        HashMap = defaultdict(int)
        for idx , val in enumerate(nums) :
            if val in HashMap :
                if abs(HashMap[val] - idx) <= k :
                    return True 
                else :
                    HashMap[val] = idx 
            else :
                HashMap[val] = idx 
        return False 