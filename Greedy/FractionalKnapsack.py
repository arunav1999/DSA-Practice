'''
Problem link: https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
'''


class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        temp = []
        for item in Items:
            temp.append((item.value,item.weight,item.value/item.weight))
        temp.sort(key = lambda x:x[2], reverse = True)
        value = 0
        curr_wt = 0
        for i in temp:
            if(i[1] + curr_wt <= W):
                curr_wt += i[1]
                value += i[0]
            else:
                diff_wt = i[1] - ((i[1] + curr_wt) - W)
                value += diff_wt * i[2]
                break
        return value
        # code here


import atexit
import io
import sys



class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))
