

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr1 = head
        ptr2 = head

        if head.next == None:
            return head

        while ptr2.next != None:
            if ptr2.next.next != None:
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next
            else:
                return ptr1.next
        return ptr1


if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    solution = Solution()
    middleNode = solution.middleNode(node1)
    print(middleNode.val)