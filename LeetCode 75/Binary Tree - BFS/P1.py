from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                # last node of the level = rightmost
                if i == size - 1:
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
