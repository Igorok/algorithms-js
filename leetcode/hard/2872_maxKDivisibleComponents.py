from typing import List
import json
from collections import deque
import heapq


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for i in range(n)]
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
        visited = [-1] * n
        res = 0

        def dfs(node, parent):
            nonlocal res

            val = values[node]
            visited[node] = 1

            for nei in adj[node]:
                if nei == parent:
                    continue
                r = dfs(nei, node)
                if r == 0:
                    res += 1
                val = (val + r) % k

            return val % k

        r = dfs(0, 0)
        if r == 0:
            res += 1

        return res



def test ():
    params = [
        {
            'input': [5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6],
            'output': 2,
        },
        {
            'input': [7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        n, edges, values, k = param['input']
        result = solution.maxKDivisibleComponents(n, edges, values, k)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
