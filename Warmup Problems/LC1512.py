class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        temp = {}
        counter = 0
        for i in range(len(nums)):
            temp[nums[i]] = 0
        for i in range(len(nums)):
            temp[nums[i]] += 1
        for j in temp:
            if(temp[j] >= 2):
                counter+=(temp[j]*(temp[j]-1))//2
        return counter
        
            