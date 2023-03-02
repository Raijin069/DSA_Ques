def getFloorAndCeil(arr, n, x):
    arr.sort()
    l=[0]*2
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<=x:
            l[0]=arr[i]
            break
    for i in range(len(arr)):
        if arr[i]>=x:
            l[1]=arr[i]
            break
    
    floor=l[0]
    ceil=l[1]
    if floor==0 and ceil!=0:
        return (-1,ceil)
    elif floor==0 and ceil==0:
        return (-1,-1)
    elif floor!=0 and ceil!=0:
        return (floor,ceil)
    else:
        return (floor,-1)

n, x = 8, 7
arr = [5, 6, 8, 9, 6, 5, 5, 6]
print(*getFloorAndCeil(arr, n, x))

