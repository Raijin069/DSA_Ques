class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        count = [0, 0, 0]
 
        ptr = head
        while ptr!=None:
            count[ptr.data]+=1
            ptr=ptr.next
        i=0
        ptr = head
        
        while ptr != None:
            if count[i] == 0:
                i+=1
            else:
                ptr.data = i 
                count[i]-=1
                ptr=ptr.next
                
        return head


class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        d = {0:0,1:0,2:0}
        start = head
        return_head = head
        while head is not None:
            d[head.data]+=1
            head = head.next
        
       
        for i in range(d[0]):
            start.data = 0
            start = start.next
        for i in range(d[1]):
            start.data = 1
            start = start.next
        for i in range(d[2]):
            start.data = 2
            start = start.next
        return return_head
                
    


