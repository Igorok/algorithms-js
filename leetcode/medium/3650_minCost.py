import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        adjReversed = [[] for i in range(n)]
        for s, e, w in edges:
            adj[s].append((e, w))
            adj[e].append((s, 2*w))

        visited = [float('inf')] * n
        visited[0] = 0
        nodesQueue = [(0, 0)]


        while nodesQueue:
            weight, node = heapq.heappop(nodesQueue)

            if visited[node] < weight:
                continue

            for nei, wght in adj[node]:
                if visited[nei] > weight + wght:
                    visited[nei] = weight + wght
                    heapq.heappush(nodesQueue, (weight + wght, nei))

            for nei, wght in adjReversed[node]:
                if visited[nei] > weight + wght:
                    visited[nei] = weight + wght
                    heapq.heappush(nodesQueue, (weight + wght, nei))



        return -1 if visited[-1] == float('inf') else visited[-1]


def test():
    params = [
        {
            "input": [4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]],
            "output": 5,
        },
        {
            "input": [4, [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]],
            "output": 3,
        },
        {
            "input": [3, [[2,1,1],[1,0,1],[2,0,16]]],
            "output": 4,
        },
    ]
    solution = Solution()

    for param in params:
        n, edges = param["input"]
        result = solution.minCost(n, edges)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
