# RECURSION

# class Solution:
#     def mergeKLists(self, lists):
#         if not lists or len(lists) == 0:
#             return None
#         return self.divide(lists, 0, len(lists) - 1)

#     def divide(self, lists, l, r):
#         if l > r:
#             return None
#         if l == r:
#             return lists[l]
#         mid = l + (r - l) // 2
#         left = self.divide(lists, l, mid)
#         right = self.divide(lists, mid + 1, r)
#         return self.conquer(left, right)

#     def conquer(self, l1, l2):
#         dummy = ListNode(0)
#         curr = dummy
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
#         if l1:
#             curr.next = l1
#         else:
#             curr.next = l2
#         return dummy.next


# DIVIDE AND CONQUER (Iteration)
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


