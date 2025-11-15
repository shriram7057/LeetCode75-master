from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        best_level = 1
        best_sum = float('-inf')

        while q:
            size = len(q)
            curr_sum = 0

            for _ in range(size):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curr_sum > best_sum:
                best_sum = curr_sum
                best_level = level

            level += 1

        return best_level
