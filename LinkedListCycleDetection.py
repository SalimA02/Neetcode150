class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      if not head or not head.next:
          return False
      
      one = head
      two = head
      
      while two and two.next:
          one = one.next
          two = two.next.next
          
          if one == two:
              return True
      
      return False
