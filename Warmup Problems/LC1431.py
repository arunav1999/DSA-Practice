class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCan = max(candies)
        new_arr = []
        for i in candies:
            if(i + extraCandies >= maxCan):
                new_arr.append(True)
            else:
                new_arr.append(False)
        return new_arr