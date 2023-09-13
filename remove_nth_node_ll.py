class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next 
        return head 


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head  
        slow = head

        len_of_ll = 0
        while fast is not None:
            len_of_ll+=1
            fast = fast.next

        if len_of_ll == n:
            head=head.next
            return head

        for i in range(len_of_ll-n-1):
            slow=slow.next
         
        slow.next = slow.next.next
        return head