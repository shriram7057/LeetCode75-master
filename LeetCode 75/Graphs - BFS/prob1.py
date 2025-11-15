from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])   # (row, col, steps)
        visited = set([(entrance[0], entrance[1])])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, d = q.popleft()

            # Check if it's an exit (boundary) and not the entrance
            if (r, c) != (entrance[0], entrance[1]):
                if r == 0 or c == 0 or r == m-1 or c == n-1:
                    return d

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n 
                    and maze[nr][nc] == '.'
                    and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))

        return -1
