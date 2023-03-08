def two_sum(nums,target):

    complementry_map = dict()
    for i in range(len(nums)):
        # complement = target - nums[i]
        if nums[i] in complementry_map:
            return [complementry_map[nums[i]],i]
        else:
            complementry_map[target - nums[i]] = i

def find_difference_pair(arr,N,l):
    # l = len(arr)
    # N = target
    arr.sort()
    i=0
    j=1
    while(i<l and j<l):
        if(arr[j]-arr[i]==N):
            print(arr[j],arr[i])
            return
        elif arr[j]-arr[i]<N:
                j+=1
        else:
            i+=1

    print("not found") 

    


