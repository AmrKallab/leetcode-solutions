# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        
    def reverse(self,head) :
        curr = head
        prev = None

        while curr :
            next_node = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_node 

        return prev

    def isPalindrome(self, head):
        if head is None or head.next is None :
            return True

        slow = head
        fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        rev = self.reverse(slow)
        while rev :
            if rev.val != head.val :
                return False 
            rev = rev.next
            head = head.next 
        return True 