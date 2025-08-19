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