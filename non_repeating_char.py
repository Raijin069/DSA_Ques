def non_repeating_char(arr: list,n: int) -> list:
    size= 2*(n+1)
    count_dict = {arr[i]:0 for i in range(size)}
    for i in range(size):
        count_dict[arr[i]] += 1
    ans_arr = [key for key,value in count_dict.items() if value==1 ]
    ans_arr.sort()
    return ans_arr

n=2
arr=[1, 2, 3, 2, 1, 4]

n = 1
arr[] = {2, 1, 3, 2}

print(*non_repeating_char(arr,n))

            
