class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

ans = Solution()
head = [3,2,0,-4]
pos = 1
print(ans.hasCycle(head,pos))