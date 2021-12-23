'''
Reverse a list using Recusrion

'''
import math as m
def reverse(arr,i,j,n):
    if(i == m.ceil(n/2)):
        return
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    reverse(arr,i+1,j-1,n)
    
arr = [1,2,3,4,5,6]
reverse(arr,0,5,6)
print(arr)