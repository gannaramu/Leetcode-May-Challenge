# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
             
        if head == None:
            return head
        
        odd = head
        even = head.next
        evenhead = even
        
        while even != None and even.next != None:
            
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = evenhead
        
        return head
#         odd_1 = ListNode(val = head.val, next=head.next) 
#         even_1 = ListNode(val = head.next.val, next=head.next.next)
#         # even_1 = head.next.next
#         # while(temp.next!=)
#         print(temp.val)
        
