def count_set_bits(n):
    count = 0

    while n>=1:

        if (n%2 == 1):
            count+=1

        n=n//2

    return count

    
print(count_set_bits(5))