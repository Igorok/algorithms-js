import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adj = [[] for i in range(n)]
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def dfs(node, parent):
            cnt = 1 if hasApple[node] else 0
            time = 0

            for nei in adj[node]:
                if nei == parent:
                    continue

                c, tm = dfs(nei, node)
                if c == 0:
                    continue

                cnt += c
                time += tm + 2
            return cnt, time

        res = dfs(0, -1)

        return res[1]


def test():
    params = [
        {
            "input": [7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]],
            "output": 8,
        },
        {
            "input": [7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]],
            "output": 6,
        },
        {
            "input": [7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        n, edges, hasApple = param["input"]
        result = solution.minTime(n, edges, hasApple)
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
