from typing import List
import json
import heapq
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for i in range(n)]
        for s, e in edges:
            adj[s].add(e)
            adj[e].add(s)

        nodesQueue = deque()

        for i in range(n):
            if len(adj[i]) == 1:
                nodesQueue.append((i, 0))

        rows = []

        while nodesQueue:
            node, length = nodesQueue.popleft()
            if len(rows) == length:
                rows.append([])
            rows[length].append(node)

            for nei in adj[node]:
                adj[nei].remove(node)
                if len(adj[nei]) == 1:
                    nodesQueue.append((nei, length+1))

        return rows[-1]





def test ():
    params = [
        {
            'input': [4, [[1,0],[1,2],[1,3]]],
            'output': [1],
        },
        {
            'input': [6, [[3,0],[3,1],[3,2],[3,4],[5,4]]],
            'output': [3,4],
        },
        {
            'input': [2, [[0,1], [1,0]]],
            'output': [0,1],
        },
        {
            'input': [
                4,
                [[0,1], [1,2], [2, 3]]
            ],
            'output': [1,2],
        },
        {
            'input': [
                5,
                [[0,1], [1,2], [2, 3], [3,4]]
            ],
            'output': [2],
        },
    ]
    solution = Solution()

    for param in params:
        n, edges = param['input']
        result = solution.findMinHeightTrees(n, edges)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
