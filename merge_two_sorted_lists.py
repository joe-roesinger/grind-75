# Solution to the Merge Two Sorted Lists problem
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Approach
# - Lists are already sorted
# - Iterate until BOTH the next attributes are None
# - check which value in the list is smaller, add that to the solution
# - When both are equal use both
# - whenever a node is used, must move down the list until next
# - Should be able to accomplish in O(n+m)
# - Might be able to reduce this to O(max(n, m))?? by nodes in a dict and doing
#   a look ahead but times would be variable and complexity not worth the effort
#
# Check that once one list is empty, theres no need to iterate, just assign the next on the solution
# to the node left on the non-None list. That gives O(max(n, m))

#----------------------------#
# Questions Class Definition #
#----------------------------#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr_node = dummy_head
        while list1 and list2:            
            list1, curr_node = self.mergeIfLower(list1, list2, curr_node)
            list2, curr_node = self.mergeIfLower(list2, list1, curr_node)

        if list1:
            curr_node.next = list1
        elif list2:
            curr_node.next = list2

        return dummy_head.next
    
    def mergeIfLower(self, list1: Optional[ListNode], list2: Optional[ListNode], curr_node: ListNode):
        if list1 and list2 and list1.val <= list2.val:
            curr_node.next = list1
            curr_node = curr_node.next
            list1 = list1.next
        
        return list1, curr_node

