# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



#### レビュー反映

class RevisedSolution(object):
    def hasCycle(self, head):
        visited = set()
        def has_cycle_helper(node):
            if not node:
                return False
            if node in visited:
                return True

            visited.add(node)
            return has_cycle_helper(node.next)

        return has_cycle_helper(head)
