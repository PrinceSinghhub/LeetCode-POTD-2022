# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ## RC ##
        ## LOGIC : START WITH BASIC EVEN AND ODD POSITIONS, FOR NEXT ODD APPEND EVENS NEXT AND FOR NEXT EVEN APPEND ODDS NEXT ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(1) ##

        if (not head): return head
        odd = head
        even = head.next
        evenHead = even
        while (even and odd and even.next and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head