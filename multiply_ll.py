MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


def multiplyTwoList(head1, head2):
    # Code here
    num1 = 0
    num2 = 0
    
    f_ptr = head1
    s_ptr = head2
    
    while f_ptr != None or s_ptr != None:
        if f_ptr != None:
            num1 = num1*10 + f_ptr.data
            f_ptr = f_ptr.next
        
        if s_ptr != None:
            num2 = num2*10 + s_ptr.data
            s_ptr = s_ptr.next
        
    return num1*num2%MOD







