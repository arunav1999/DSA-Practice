'''
Problem Statement link: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

'''

def nmeetings(n, start, finish):
    k = 0
    temp = []
    for i in range(n):
        temp.append((start[i], finish[i], k))
        k+=1
    temp.sort(key = lambda temp: temp[1])
    end = temp[0][1]
    possible_meetings = 1
    for i in range(1,len(temp)):
        if(temp[i][0] > end):
            possible_meetings += 1
            end = temp[i][1]
    return possible_meetings

s = [1 ,3 ,0 ,5 ,8 ,5]
f = [2 ,4 ,6 ,7 ,9 ,9]

print(nmeetings(3,s,f))