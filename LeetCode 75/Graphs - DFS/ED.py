class Solution(object):
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque

        graph = defaultdict(list)

        # Build graph: a/b = v  →  a->b (v),  b->a (1/v)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        # Function to evaluate a query using BFS
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited = set()
            q = deque([(start, 1.0)])  # (node, product so far)

            while q:
                node, prod = q.popleft()

                if node == end:
                    return prod

                visited.add(node)

                for nei, weight in graph[node]:
                    if nei not in visited:
                        q.append((nei, prod * weight))

            return -1.0

        # Process each query
        return [bfs(a, b) for a, b in queries]
