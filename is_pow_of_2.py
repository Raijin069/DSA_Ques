def is_pow_of_2(n):
    return ((n>0) and ((n&(n-1))==0)) 

for i in range(int(input("enter num"))):
    print(f"{i} = {is_pow_of_2(i)}")

