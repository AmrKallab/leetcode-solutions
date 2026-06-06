class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for key,freq in counter.items() :
            bucket[freq].append(key) 

        res = []
        for i in range(len(bucket)-1,-1,-1) :
            
            for num in bucket[i] :
                res.append(num)
                k -= 1
                if k == 0 :
                    return res
        