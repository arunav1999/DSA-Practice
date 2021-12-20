'''
Problem statement link: https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

'''

def minimumPlatforms(n,arr,dep):
    arr.sort()
    dep.sort()
    p1 = 0
    p2 = 1
    platforms = 1
    minimumPlatforms = 1
    while(p2 < len(arr) and p1 < len(dep)):
        if(arr[p2] <= dep[p1]):
            platforms+=1
            p2 += 1
        else:
            p1 += 1
            platforms -= 1
        minimumPlatforms = max(minimumPlatforms,platforms)
    return minimumPlatforms

n = 3
arr = [900, 1100, 1235]
dep = [1000, 1200, 1240]

print(minimumPlatforms(n,arr,dep))        

