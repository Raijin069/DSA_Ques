from math import log2
def bit_difference(a,b):
    return int(log2(a^b))

print(bit_difference(10,20))
print(bit_difference(20,25))