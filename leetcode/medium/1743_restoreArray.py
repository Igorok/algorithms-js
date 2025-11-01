from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = {}
        for s, e in adjacentPairs:
            adj[s] = adj.get(s, [])
            adj[s].append(e)

            adj[e] = adj.get(e, [])
            adj[e].append(s)

        start = None
        for k in adj:
            if len(adj[k]) == 1:
                start = k
                break

        visited = set()

        res = []
        def dfs(num):
            res.append(num)
            for nei in adj[num]:
                if not nei in visited:
                    visited.add(nei)
                    dfs(nei)

        visited.add(start)
        dfs(start)

        return res

'''

1 1 0 1 1 0 0
0 0 1 0 0

'''



def test ():
    params = [
        {
            'input': [[2,1],[3,4],[3,2]],
            'output': [1,2,3,4],
        },
        {
            'input': [[4,-2],[1,4],[-3,1]],
            'output': [-2,4,1,-3],
        },
        {
            'input': [[100000,-100000]],
            'output': [100000,-100000],
        },
    ]
    solution = Solution()

    for param in params:
        adjacentPairs = param['input']
        result = solution.restoreArray(adjacentPairs)
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
