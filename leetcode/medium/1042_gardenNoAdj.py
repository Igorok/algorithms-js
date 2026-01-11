from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        colors = [0] * (n+1)
        adj = [[] for i in range(n+1)]

        for s, e in paths:
            adj[s].append(e)
            adj[e].append(s)

        def paint(root):
            nodesQueue = deque()
            nodesQueue.append(root)

            while nodesQueue:
                node = nodesQueue.popleft()
                available = [1] * 5
                for nei in adj[node]:
                    if colors[nei] == 0:
                        nodesQueue.append(nei)
                    else:
                        available[colors[nei]] = 0

                for i in range(1, 5):
                    if available[i] == 1:
                        colors[node] = i
                        break

        for i in range(1, n+1):
            if colors[i] == 0:
                paint(i)

        return colors[1:]


def test ():
    params = [
        {
            'input': [3, [[1,2],[2,3],[3,1]]],
            'output': [1,2,3],
        },
        {
            'input': [4, [[1,2],[3,4]]],
            'output': [1,2,1,2],
        },
        {
            'input': [4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]],
            'output': [1,2,3,4],
        },
        {
            'input': [1, []],
            'output': [1],
        },
        {
            'input': [3, []],
            'output': [1,1,1],
        },
    ]
    solution = Solution()

    for param in params:
        n, paths = param['input']
        result = solution.gardenNoAdj(n, paths)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
