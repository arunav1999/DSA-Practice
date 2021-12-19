def nmeetings(n, start, finish):
    k = 0
    temp = []
    for i in range(n):
        temp.append((start[i], finish[i],finish[i]-start[i] ,k))
        k+=1
    temp.sort(key = lambda temp: temp[2])
    end = 0
    possible_meetings = 0
    for entry in temp:
        if(entry[0] > end):
            possible_meetings += 1
            end = entry[1]
    return possible_meetings

s = [10, 12, 20]
f = [20, 25, 30]

print(nmeetings(3,s,f))