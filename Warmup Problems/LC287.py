class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums[abs(nums[i])] >= 0):
                nums[abs(nums[i])] = -1 * nums[abs(nums[i])]
            else:
                return abs(nums[i])
                                    