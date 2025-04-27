class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        dummy = head
        change = dummy

        while change:
            stack.append(change.val)
            change = change.next

            if len(stack) == k:
                while stack:
                    dummy.val = stack.pop()
                    dummy = dummy.next
        return head

# THIS REVERSES THE VALUES NOT THE ACTUAL NODES
