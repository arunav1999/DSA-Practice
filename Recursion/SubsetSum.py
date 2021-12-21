'''
Problem Statement: https://practice.geeksforgeeks.org/problems/subset-sums2234/1

'''

class Solution:
    
    def recursionHelper(self,index,sumi,subset,arr,N):
        if(index == N):
            subset.append(sumi)
            return
        self.recursionHelper(index+1,sumi+arr[index],subset,arr,N)
        self.recursionHelper(index+1,sumi,subset,arr,N)
    
    def subsetSums(self, arr, N):
        temp = []
        self.recursionHelper(0,0,temp,arr,N)
        temp.sort()
        return temp
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

