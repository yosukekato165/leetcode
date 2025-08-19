# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        def depthFirstSearch(node, visited):
            if not node:
                return False
            if node in visited:
                return True

            visited.add(node)
            return depthFirstSearch(node.next, visited)

        return depthFirstSearch(head, set())
