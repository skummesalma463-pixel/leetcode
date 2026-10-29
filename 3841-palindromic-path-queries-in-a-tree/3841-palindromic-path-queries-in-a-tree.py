class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        timer = 0

        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[0][u] = p
                tin[u] = timer
                order.append(u)
                timer += 1

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))

        # Build ancestor table
        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        # Recalculate subtree intervals using iterative DFS
        timer = 0
        stack = [(0, 0, False)]

        while stack:
            u, p, exiting = stack.pop()

            if not exiting:
                tin[u] = timer
                timer += 1
                stack.append((u, p, True))

                for v in reversed(graph[u]):
                    if v != p:
                        stack.append((v, u, False))
            else:
                tout[u] = timer - 1

        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def letter_mask(c):
            return 1 << (ord(c) - ord('a'))

        chars = list(s)
        masks = [letter_mask(c) for c in chars]

        for u in range(n):
            add(tin[u], masks[u])
            if tout[u] + 1 < n:
                add(tout[u] + 1, masks[u])

        def is_ancestor(u, v):
            return tin[u] <= tin[v] <= tout[u]

        def lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v

            for j in range(LOG - 1, -1, -1):
                a = parent[j][u]
                if not is_ancestor(a, v):
                    u = a

            return parent[0][u]

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = letter_mask(c)
                change = masks[u] ^ new_mask

                add(tin[u], change)
                if tout[u] + 1 < n:
                    add(tout[u] + 1, change)

                chars[u] = c
                masks[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)
                mask = prefix(tin[u]) ^ prefix(tin[v]) ^ masks[ancestor]

                answer.append((mask & (mask - 1)) == 0)

        return answer