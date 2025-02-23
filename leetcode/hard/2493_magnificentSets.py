from typing import List
import json
from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        visited = [0]*(n+1)
        adj = [[] for i in range(n+1)]
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def getNodes(id):
            visited[id] = 1
            nodes = set()
            nodes.add(id)
            nodesQueue = deque([id])

            while nodesQueue:
                i = nodesQueue.popleft()
                for nei in adj[i]:
                    if nei in nodes:
                        continue
                    nodes.add(nei)
                    visited[nei] = 1
                    nodesQueue.append(nei)

            return nodes

        def getLength(id):
            maxLevel = 1
            levels = {
                id: 1,
            }
            nodesQueue = deque([(id, 1)])

            while nodesQueue:
                i, level = nodesQueue.popleft()
                maxLevel = level

                for nei in adj[i]:
                    if nei in levels:
                        if abs(levels[nei] - levels[i]) != 1:
                            return -1
                        else:
                            continue
                    levels[nei] = level + 1
                    nodesQueue.append((nei, level + 1))

            return maxLevel

        res = 0
        for i in range(1, n+1):
            if visited[i] == 1:
                continue
            nodes = getNodes(i)
            length = 1
            for j in nodes:
                r = getLength(j)
                if r == -1:
                    return -1
                length = max(length, r)
            res += length

        return res

'''
    14
    13
    12
      10 11
        1
       2 3
    4 5      6 7
    8       9
'''

def test ():
    params = [
        {
            'input': [6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]],
            'output': 4,
        },
        {
            'input': [3, [[1,2],[2,3],[3,1]]],
            'output': -1,
        },
        {
            'input': [2, [[1, 2]]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        n, edges = param['input']
        result = solution.magnificentSets(n, edges)
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
