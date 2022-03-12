# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        flag = 1
        while p1 and p2:
            if p1 == p2:
                return p1
            if not p1.next and flag:
                p1 = headB
                flag = 0
            else:
                p1 = p1.next
            if not p2.next:
                p2 = headA
            else:
                p2 = p2.next

        return p1


if __name__ == '__main__':
    solu = Solution()
    headA = ListNode(1)
    headA.next = ListNode(9)
    headA.next.next = ListNode(1)
    headB = ListNode(3)
    headC = ListNode(2)
    headC.next = ListNode(4)
    headA.next.next.next = headC
    headB.next = headC
    print(solu.getIntersectionNode(headA, headB).val)
