def find_1_unique(arr):
    xor_sum = 0
    for i in range(len(arr)):
        xor_sum^=arr[i]
    return xor_sum 

def set_bit(n,pos):
    return (n&(1<<pos))!=0  


def find_2_unique(arr):
    xor_sum = 0
    for i in range(len(arr)):
        xor_sum^=arr[i]
    temp=xor_sum
    setbit = 0
    pos = 0
    while setbit!=1:
        setbit = xor_sum & 1
        pos+=1
        xor_sum>>=1

    new_xor=0    
    for i in range(len(arr)):
        if set_bit(arr[i],pos-1) == 1:
            new_xor^=arr[i]
    return new_xor^temp,new_xor


arr_1 = [1,2,3,3,2,6,1]
print(find_1_unique(arr_1))

arr_1.append(7)
print(*find_2_unique(arr_1))
