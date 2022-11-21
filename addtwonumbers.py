# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        temp1c = 1
        temp2c = 1
        
        def helper(l1, rem):
            if l1:
                l1.val += rem
                rem += 0
                if l1.val >= 10:
                    l1.val %= 10
                    rem = 1
                    if l1.next:
                        helper(l1.next, rem)
                    else:
                        nextNode = ListNode(1)
                        l1.next = nextNode
                        l1 = nextNode
            return l1
        
        def recurnext(l1, l2, rem):
            l1.val += l2.val
            l1.val += rem
            rem = 0
            if l1.val >= 10:
                rem = 1
                l1.val %= 10
            if l2.next:
                recurnext(l1.next, l2.next, rem)
            elif rem == 1:
                if l1.next:
                    helper(l1.next, rem)
                else:
                    nextNode = ListNode(1)
                    l1.next = nextNode
            return l1
        
        while temp1.next:
            temp1c += 1
            temp1 = temp1.next
        while temp2.next:
            temp2c += 1
            temp2 = temp2.next
        if temp1c >= temp2c:
            return recurnext(l1, l2, 0)
        else:
            return recurnext(l2, l1, 0)