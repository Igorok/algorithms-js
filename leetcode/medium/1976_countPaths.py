from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        modulo = 7 + 10e8
        adj = [[] for i in range(n)]
        for s, e, w in roads:
            adj[s].append((w, e))
            adj[e].append((w, s))

        pathWeight = [float('inf')] * n
        pathWeight[0] = 0

        pathCount = [0] * n
        pathCount[0] = 1

        nodesHeap = [(0, 0)]

        while nodesHeap:
            weight, node = heapq.heappop(nodesHeap)
            for wei, nei in adj[node]:
                newWeight = weight + wei
                if pathWeight[nei] == newWeight:
                    pathCount[nei] = int((pathCount[nei] + pathCount[node]) % modulo)
                elif pathWeight[nei] > newWeight:
                    pathWeight[nei] = newWeight
                    pathCount[nei] = pathCount[node]
                    heapq.heappush(nodesHeap, (newWeight, nei))

        return pathCount[n-1]


def test ():
    params = [
        {
            'input': [7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]],
            'output': 4,
        },
        {
            'input': [2, [[1,0,10]]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        n, roads = param['input']
        result = solution.countPaths(n, roads)
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
