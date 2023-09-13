# class stack:
#     def __init__(self,size):
#         self.size = size
#         self.data = [None]*self.size ## makes stackk faster by preallocation
#         self.min_s = [None]*self.size 
#         self.top=-1
#         self.mini = 1_00_000 # random big number

#     def is_empty(self):
#         return self.top == -1
    
#     def is_full(self):
#         return self.top == self.size - 1
    
#     def push(self,val):
#         if self.is_full():
#             print('stack overflow')
#             return
        
#         self.top+=1
#         self.data[self.top] = val
#         self.mini = min(self.mini,val)
#         self.min_s[self.top] = self.mini

#     def get_min(self):
#         if self.is_empty():
#             print('stack empty')
#             return

#         return self.min_s[self.top]        
    
#     def pop(self):
#         if self.is_empty():
#             print('stack underflow')
#             return
        
#         self.top-=1 ## no need to update poped value
        
#     def print_top(self):
#         if self.is_empty():
#             print('stack empty')
#             return
        
#         return self.data[self.top]

#     def print_s(self):
#         if self.is_empty():
#             print('stack empty')
#             return
    
#         return self.data[:self.top]

class stack:
    def __init__(self,size):
        self.size = size
        self.data = [None]*self.size
        self.top=-1
        self.mini = 1_00_000 # random big number

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.size - 1
    
    def push(self,val):
        if self.is_full():
            print('stack overflow')
            return
        
        self.top+=1
        if self.mini > val:
            self.data[self.top] = (2*val)-self.mini
            self.mini = val
        else:
            self.data[self.top] = val


    def get_min(self):
        if self.is_empty():
            print('stack empty')
            return

        return self.mini        
    
    def pop(self):
        if self.is_empty():
            print('stack underflow')
            return
        
        if self.data[self.top] < self.mini:
            self.mini = (2*self.mini)-self.data[self.top]
        self.top-=1
            
        
    def print_top(self):
        if self.is_empty():
            print('stack empty')
            return
        
        return self.data[self.top]

    def print_s(self):
        if self.is_empty():
            print('stack empty')
            return
    
        return self.data[:self.top]

s = stack(5)   
s.push(5)
s.push(3)
s.push(8)
s.push(2)
s.push(4)

while(s.is_empty() is False):
    print(s.print_s())
    print(s.get_min())
    s.pop()
    print('\n')
    
