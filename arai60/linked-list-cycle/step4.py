class Solution(object):
    def hasCycle(self, head):
        visited = set()
        node = head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False

## 指摘反映

class Solution(object):
    def hasCycle(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
        