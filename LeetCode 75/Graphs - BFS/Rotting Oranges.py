from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: collect all rotten oranges & count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0  # no fresh oranges

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        # Step 2: BFS rotting process
        while q:
            r, c, minutes = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2        # orange becomes rotten
                    fresh -= 1
                    q.append((nr, nc, minutes + 1))

        # Step 3: if fresh still remains -> impossible
        return minutes if fresh == 0 else -1
