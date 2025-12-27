"""Task 743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1."""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 10**10
        mini = {i: INF for i in range(1, n + 1)}

        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        def dfs(node, cur):
            if cur >= mini[node]:
                return
            mini[node] = cur
            for nxt, w in graph[node]:
                dfs(nxt, cur + w)

        dfs(k, 0)

        if any(v == INF for v in mini.values()):
            return -1

        return max(mini.values())