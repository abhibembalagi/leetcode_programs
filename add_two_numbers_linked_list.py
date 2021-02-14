# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultant_list=current_node=ListNode(0)
        carry=0
        while l1 or l2:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            current_node.next=ListNode(carry%10)
            current_node=current_node.next
            carry=carry//10
        if carry>0:
            current_node.next=ListNode(carry)
        return resultant_list.next
