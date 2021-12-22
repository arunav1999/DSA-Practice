class Solution:
    def recursionHelper(self,index, arr, target, ans, ds):
        if(index == len(arr)):
            if(target == 0):
                ans.append(copy.deepcopy(ds))
            return
        if(arr[index] <= target):
            ds.append(arr[index])
            self.recursionHelper(index,arr,target - arr[index],ans,ds)
            ds.pop(len(ds) -1)
        self.recursionHelper(index +1,arr,target,ans,ds)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.recursionHelper(0,candidates,target,ans,[])
        return ans
        