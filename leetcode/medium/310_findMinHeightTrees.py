from typing import List
import json
import heapq
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        val = float('inf')
        res = []

        def dfs(node, parent, path):
            nonlocal val, res, adj

            localPath = 0
            for nei in adj[node]:
                if nei == parent:
                    continue

                r = dfs(nei, node, path + 1)
                localPath = max(localPath, r)

            height = max(path, localPath)

            if height == val:
                res.append(node)
            elif height < val:
                val = height
                res = [node]

            return localPath + 1

        dfs(0, 0, 0)


        return res





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
