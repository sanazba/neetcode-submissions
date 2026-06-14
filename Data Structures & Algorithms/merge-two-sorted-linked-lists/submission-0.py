# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = node = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next #	اشاره‌گر node هم یک قدم جلو می‌رود.

            node.next = list1 or list2 #اگر یکی از لیست‌ها تمام شده باشد،
            return dummy.next

            # چون dummy فقط یک نگه‌دار اولیه بود، ابتدای واقعی لیست از dummy.next شروع می‌شود.

            
        