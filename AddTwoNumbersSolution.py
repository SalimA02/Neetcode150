class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        new_head = head.next
        copy = new_head
        while curr:
            curr.next = copy.next
            curr = curr.next
            if curr:
                copy.next = curr.next
                copy = copy.next

        return new_head
