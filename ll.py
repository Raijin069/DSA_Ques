class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class Singly_LL:
    def __init__(self):
        self.head = None


    def size(self):
        if self.head is None:
            return 0
        count = 0
        start = self.head
        while start is not None:
            start=start.next
            count+=1
        return count 

    def is_empty(self):
        return self.size() == 0   


    def print_ll(self):
        # if self.head is None:
        #     print("list is empty")
        #     return
        if self.is_empty() is True:
            print("list is empty")
            return
        start = self.head
        while start is not None:
            print(start.data,end = " -> ")
            start=start.next
        print("None")

            
    def insert_last(self,num):
        new_node = Node(num)
        # if self.head is None:
        #     self.head = new_node
        #     return
        if self.is_empty() is True:
            self.head = new_node
            return

        start = self.head
        while start.next is not None:
            # print(start.data)
            start=start.next   
        start.next=new_node


    def reverse_ll(self):
        if (self.head is None) or (self.head.next is None):
            print("already reversed")
            return
        prev = self.head
        curr = self.head.next
        while curr is not None:
            next = curr.next
            curr.next = prev

            # update
            prev = curr
            curr = next

        self.head.next = None
        self.head = prev      

ll1 = Singly_LL()
print(ll1.is_empty())
ll1.insert_last(1) 
ll1.insert_last(2) 
ll1.insert_last(3) 
ll1.insert_last(4)
ll1.print_ll()
ll1.reverse_ll()
ll1.print_ll()
print(ll1.size())
print(ll1.is_empty())