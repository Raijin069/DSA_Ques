from math import log2
def count_set_bit(n):
    # bin_rep = ""
    # while n>=1:
    #     bin_rep+=str(n%2)
    #     n=n//2
    # length_of_binary = len(bin_rep)    
    # bin_rep = bin_rep[::-1]
    # count = 0
    # for i in range(length_of_binary):
    #     curr_pos = int(bin_rep[length_of_binary-(i+1)])
    #     if curr_pos & 1==1:
    #         count+=1
    #         pos = i+1
    # return pos if count == 1 else -1
    if ((n>0) and ((n&(n-1))==0)):
        return int(log2(n)) + 1
    return -1         



print(count_set_bit(7))