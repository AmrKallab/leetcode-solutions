class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        a = [0] * num_people
        cnt = 1
        i = 0
        while candies > 0 :
            if candies > cnt : 
                a[i] += cnt
                candies -= cnt 
                cnt += 1
            else :
                a[i] += candies 
                break
            
            if i == num_people - 1 :
                i = 0
            else :
                i += 1

        return a
