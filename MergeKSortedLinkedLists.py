# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         nodes = []
#         for lst in lists:
#             while lst:
#                 nodes.append(lst.val)
#                 lst = lst.next
#         nodes.sort()

#         res = ListNode(0)
#         cur = res
#         for node in nodes:
#             cur.next = ListNode(node)
#             cur = cur.next
#         return res.next
#ITERATION
# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         res = ListNode(0)
#         cur = res
        
#         while True:
#             minNode = -1
#             for i in range(len(lists)):
#                 if not lists[i]:
#                     continue
#                 if minNode == -1 or lists[minNode].val > lists[i].val:
#                     minNode = i
            
#             if minNode == -1:
#                 break
#             cur.next = lists[minNode]
#             lists[minNode] = lists[minNode].next
#             cur = cur.next

#         return res.next

# RECURSION

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = l + (r - l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)
        return self.conquer(left, right)

    def conquer(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next


