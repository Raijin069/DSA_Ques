def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
 
        set1 = set()
 
        current = head
        set1.add(head.data)
 
        while current.next is not None:
 
            if current.next.data in set1:
                current.next = current.next.next
            else:
                set1.add(current.next.data)
                current = current.next
 
        return head