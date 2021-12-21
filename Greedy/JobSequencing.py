def jobScheduling(jobs, n):
    arr = jobs
    arr.sort(key = lambda x: x[2], reverse = True)
    max_deadline = 0
    for i in arr:
        max_deadline = max(max_deadline,i[1])
    aux = [-1 for i in range(1,max_deadline+1)]
    total_profit = 0
    for i in range(len(arr)):
        for j in range(arr[i][1]-1,-1,-1):
            if(aux[j] == -1):
                aux[j] = arr[i][0]
                total_profit += arr[i][2]
                break
    return (total_profit,aux)


jobs = [(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)]
print(jobScheduling(jobs,len(jobs)))