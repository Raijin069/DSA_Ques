def count_total_set_bits(n):
    if n==0:
        return 0
    x=largest_power_of_2_in_range(n)
    above_2_x = x * (1<<(x-1))
    below_2_x = n-(1<<x)+1
    rest = below_2_x-1
    return above_2_x+below_2_x+count_total_set_bits(rest)
 

def largest_power_of_2_in_range(n):
    x=0
    while (1<<x)<=n:
        x+=1

    return x-1               

print(count_total_set_bits(8))    