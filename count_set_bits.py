def count_set_bits(n):
    # count = 0

    # while n>=1:

    #     if (n%2 == 1):
    #         count+=1

    #     n=n//2

    # return count
    count=0
    while n!=0:
        n= n&(n-1)
        count+=1
    return count    
    
print(count_set_bits(7))