def no_fo_zeros(n):
    count=0
    while n&1!=1:
        n=n>>1
        count+=1
    return count    


n=8
print(no_fo_zeros(n))