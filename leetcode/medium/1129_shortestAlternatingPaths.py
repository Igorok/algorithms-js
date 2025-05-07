import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = [[], []]
        adj[0] = [[] for i in range(n)]
        for s, e in redEdges:
            adj[0][s].append(e)
        adj[1] = [[] for i in range(n)]
        for s, e in blueEdges:
            adj[1][s].append(e)

        nodesQueue = deque()
        nodesQueue.append((0, 0, 0))
        nodesQueue.append((0, 1, 0))

        res = [-1] * n
        visited = [[], []]
        visited[0] = [-1] * n
        visited[0][0] = 1
        visited[1] = [-1] * n
        visited[1][0] = 1
        while nodesQueue:
            node, color, length = nodesQueue.popleft()
            if res[node] == -1:
                res[node] = length
            else:
                res[node] = min(res[node], length)

            nextColor = 1 if color == 0 else 0
            for nei in adj[nextColor][node]:
                if visited[nextColor][nei] == -1:
                    visited[nextColor][nei] = 1
                    nodesQueue.append((nei, nextColor, length + 1))

        return res

def test ():
    params = [
        {
            'input': [3, [[0,1],[1,2]], []],
            'output': [0,1,-1],
        },
        {
            'input': [3, [[0,1]], [[2,1]]],
            'output': [0,1,-1],
        },
    ]
    solution = Solution()

    for param in params:
        n, redEdges, blueEdges = param['input']

        result = solution.shortestAlternatingPaths(n, redEdges, blueEdges)
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
