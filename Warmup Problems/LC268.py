class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_sum = (n*(n+1))//2
        missing = n_sum - sum(nums)
        if(0 not in nums):
            return 0
        return missing