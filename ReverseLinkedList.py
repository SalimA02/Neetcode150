class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []:
            return []

        prev, current = None, head
      
        while current:
            Next = current.next 
            current.next = prev
            prev = current
            current = Next

        return prev
