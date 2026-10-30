import heapq
from typing import List


class Solution:

  def shortestPath(
      self, n: int, edges: List[List[int]], labels: str, k: int
  ) -> int:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
      adj[u].append((v, w))

    # dist[u][c] stores the minimum cost to reach node u with run count c
    dist = [[float("inf")] * (k + 1) for _ in range(n)]
    dist[0][1] = 0

    # Priority queue stores (cost, u, count)
    pq = [(0, 0, 1)]

    while pq:
      d, u, count = heapq.heappop(pq)

      if u == n - 1:
        return d

      if d > dist[u][count]:
        continue

      for v, w in adj[u]:
        next_count = count + 1 if labels[u] == labels[v] else 1

        if next_count <= k:
          new_dist = d + w
          if new_dist < dist[v][next_count]:
            dist[v][next_count] = new_dist
            heapq.heappush(pq, (new_dist, v, next_count))

    return -1