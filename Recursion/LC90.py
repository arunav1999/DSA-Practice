class Solution:
    def recursionHelper(self,index,nums,ds,ans):
        ans.append(ds)
        for i in range(index,len(nums)):
            if(i!=index and nums[i]==nums[i-1]) continue;
            ds.append(nums[i])
            recursionHelper(i+1,nums,ds,ans)
            ds.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        recursionHelper(0,nums,[],ans)
        return ans
        