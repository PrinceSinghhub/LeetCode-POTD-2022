# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        p1, p2 = headA, headB
        while p1 or p2:
            if p1 == p2:
                return p1
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
