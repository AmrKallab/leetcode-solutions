class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left , right = 0 , len(people) - 1
        num_of_boat = 0
        while left <= right :
            if people[left] + people[right] > limit :
                right -= 1
                num_of_boat += 1
            else :
                left , right = left + 1, right - 1
                num_of_boat += 1
        return num_of_boat