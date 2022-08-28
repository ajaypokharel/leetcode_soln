"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 

Return the linked list sorted as well.

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        if not head or not head.next:
            return head
        
        while current != None and current.next != None:
            while current.val == current.next.val:
                if current.val == current.next.val:
                    if current.next.next:
                        current.next = current.next.next
                    else:
                        current.next = None
                        break

            current = current.next
                    
        return head
            