import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        adj = [[] for _ in range(N)]
        for p1, p2 in pairs:
            adj[p1].append(p2)
            adj[p2].append(p1)

        visited = [0]*N
        id = 0
        data = {}

        def dfs(node, id):
            nonlocal visited, data, adj, s

            for nei in adj[node]:
                if visited[nei] != 0:
                    continue
                visited[nei] = id
                data[id].append(s[nei])
                dfs(nei, id)

        for i in range(N):
            if visited[i] != 0:
                continue
            id += 1
            visited[i] = id
            data[id] = [s[i]]
            dfs(i, id)

        for key in data:
            data[key].sort(key=lambda x: -ord(x))

        # print('data', data)

        res = []
        for i in range(N):
            id = visited[i]
            res.append(data[id].pop())

        return ''.join(res)


def test():
    params = [
        {
            "input": ["dcab", [[0,3],[1,2]]],
            "output": 'bacd',
        },
        {
            "input": ["dcab", [[0,3],[1,2],[0,2]]],
            "output": 'abcd',
        },
        {
            "input": ["cba", [[0,1],[1,2]]],
            "output": 'abc',
        },
    ]
    solution = Solution()

    for param in params:
        s, pairs = param["input"]
        result = solution.smallestStringWithSwaps(s, pairs)

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
