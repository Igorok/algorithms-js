from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]

        for s, e, w in edges:
            adj[s].append((e, w))
            adj[e].append((s, w))

        def getPath(start: int, end: int):
            if start == end:
                return 0

            visited = [-1] * n
            queueNodes = []
            for node, weight in adj[start]:
                heapq.heappush(queueNodes, (weight, node))

            res = float('inf')
            while queueNodes:
                path, node = heapq.heappop(queueNodes)
                if node == end:
                    res = min(res, path)
                    # continue

                for nei, weigth in adj[node]:
                    newPath = weight & path
                    if visited[nei] == -1 or visited[nei] > newPath:
                        visited[nei] = newPath
                        heapq.heappush(queueNodes, (newPath, node))

            return -1 if res == float('inf') else res




        return [getPath(s, e) for s, e in query]


    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]

        parents = [-1] * n
        deeps = [0] * n
        weights = [-1] * n

        def getParent(node):
            if parents[node] == -1:
                return node

            visited = []
            while parents[node] != -1:
                visited.append(node)
                node = parents[node]

            for child in visited:
                parents[child] = node

            return node

        def union(start, end, weight):
            p1 = getParent(start)
            p2 = getParent(end)
            if p1 == start and p2 == end and deeps[start] == 0 and deeps[end] == 0:
                parents[start] = end
                weights[end] = weight
                deeps[end] = 1
                return

            p1, p2 = [p1, p2] if deeps[p1] > deeps[p2] else [p2, p1]

            weights[p1] &= weight
            if start != p1:
                parents[start] = p1
            if end != p1:
                parents[end] = p1

            if p1 == p2:
                return

            parents[p2] = p1

            if deeps[p2] == 0:
                deeps[p1] += 1
            else:
                weights[p1] &= weights[p2]

            return

        def getPath(start, end):
            p1 = getParent(start)
            p2 = getParent(end)

            if p1 == p2:
                return weights[p1]
            else:
                return -1

        for s, e, w in edges:
            union(s, e, w)

        return [getPath(s, e) for s, e in query]

'''


110
101
001


0 1 1
1 3 2

'''


def test ():
    params = [
        {
            'input': [3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]],
            'output': [0],
        },
        {
            'input': [5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]]],
            'output': [1,-1],
        },

    ]
    solution = Solution()

    for param in params:
        n, edges, query = param['input']
        result = solution.minimumCost(n, edges, query)
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
