from typing import List
import json
from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]

        def find(id):
            if parents[id] != id:
                parents[id] = find(parents[id])
            return parents[id]

        def union(s, e):
            p1 = find(s)
            p2 = find(e)
            if p1 == p2:
                return True

            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]
                parents[p1] = p2
            else:
                rank[p1] += rank[p2]
                parents[p2] = p1

            return False

        for s, e in edges:
            if union(s,e):
                return [s, e]

        return []

def test ():
    params = [
        {
            'input': [[1,2],[1,3],[2,3]],
            'output': [2,3],
        },
        {
            'input': [[1,2],[2,3],[3,4],[1,4],[1,5]],
            'output': [1,4],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findRedundantConnection(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
