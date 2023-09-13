class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        flag = 0
        slow = head
        fast = head

        while (fast is not None) and (fast.next is not None):
            slow=slow.next
            fast = fast.next.next

            if slow==fast:
                flag=1
                slow = head
                break
        if flag == 1:
            while slow != fast:
                slow = slow.next
                fast = fast.next
                
            while slow.next!= fast:
                slow=slow.next
                
            slow.next = None
        return