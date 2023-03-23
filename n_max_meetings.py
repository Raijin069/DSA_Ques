# ans = []
start = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]
n = len(start)
l = [[None for i in range(3)] for _ in range(n)]
for i in range(n):
    l[i][0] = start[i]
    l[i][1] = finish[i]
    l[i][2] = i+1

def maxMeeting(l, n):
    ans = []
    l.sort(key = lambda x: x[1])
    ans.append(l[0][2])
    time_limit = l[0][1]
    
    for i in range(1, n):
        if l[i][0] > time_limit:
            ans.append(l[i][2])
            time_limit = l[i][1]

    for i in ans:
        print(i,end =" ")
    print()

maxMeeting(l,len(l))


