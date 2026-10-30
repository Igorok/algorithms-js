import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for i in range(n)]
        for s, e, w in edges:
            adj[s].append((e, w))

        queue = [(0, 1, 0)]
        visited = [{} for i in range(n)]

        while queue:
            weight, repeat, node = heapq.heappop(queue)

            if node == n - 1:
                return weight

            for nei, w in adj[node]:
                new_repeat = 1 if labels[node] != labels[nei] else repeat + 1
                if new_repeat > k:
                    continue

                new_weight = weight + w
                if (
                    new_repeat in visited[nei]
                    and visited[nei][new_repeat] <= new_weight
                ):
                    continue

                visited[nei][new_repeat] = new_weight
                heapq.heappush(queue, (new_weight, new_repeat, nei))

        return -1


def test():
    params = [
        {
            "input": [3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1],
            "output": 3,
        },
        {
            "input": [3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2],
            "output": 2,
        },
        {
            "input": [3, [[0, 1, 1], [1, 2, 1]], "aaa", 2],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        n, edges, labels, k = param["input"]
        result = solution.shortestPath(n, edges, labels, k)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
