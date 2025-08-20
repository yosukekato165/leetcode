# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class TwoPointerSolution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

class RecursionSolution(object):
    def hasCycle(self, head):
        visited = set()
        node = head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
