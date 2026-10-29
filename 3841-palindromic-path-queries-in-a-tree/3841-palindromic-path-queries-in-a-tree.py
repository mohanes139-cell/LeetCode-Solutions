import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (size + 2)

    def update(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] ^= delta
            idx += idx & (-idx)

    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & (-idx)
        return res

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 17  # Since n <= 5 * 10^4, 2^16 > 50000
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative or DFS setup for LCA and Euler tour
        # Using iterative traversal to safely avoid stack limits in Python
        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True

        # BFS/topological traversal to set parents and depth
        queue = [0]
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    parent[nxt] = curr
                    depth[nxt] = depth[curr] + 1
                    queue.append(nxt)

        # Build binary lifting table
        for i in range(n):
            up[i][0] = parent[i] if parent[i] != -1 else 0
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        # Non-recursive DFS to compute tin and tout
        timer = 1
        it_stack = [(0, 0)]  # (node, edge_index)
        tin[0] = timer
        timer += 1

        while it_stack:
            curr, edge_idx = it_stack[-1]
            if edge_idx < len(adj[curr]):
                nxt = adj[curr][edge_idx]
                it_stack[-1] = (curr, edge_idx + 1)
                if nxt != parent[curr]:
                    tin[nxt] = timer
                    timer += 1
                    it_stack.append((nxt, 0))
            else:
                tout[curr] = timer - 1
                it_stack.pop()

        chars = list(s)
        node_mask = [1 << (ord(c) - ord('a')) for c in chars]

        bit = FenwickTree(n)

        # Range XOR update in BIT: [l, r] ^= val
        def range_update(l: int, r: int, val: int):
            bit.update(l, val)
            bit.update(r + 1, val)

        # Initialize subtree masks
        for i in range(n):
            range_update(tin[i], tout[i], node_mask[i])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                new_m = 1 << (ord(new_c) - ord('a'))
                delta = node_mask[u] ^ new_m
                if delta:
                    range_update(tin[u], tout[u], delta)
                    node_mask[u] = new_m
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                # Path XOR = P(u) ^ P(v) ^ mask(lca)
                path_xor = bit.query(tin[u]) ^ bit.query(tin[v]) ^ node_mask[lca]
                
                # Palindrome check: at most 1 bit set
                ans.append(path_xor == 0 or (path_xor & (path_xor - 1)) == 0)

        return ans