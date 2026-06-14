import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List
import math


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        N = len(edges)+2
        M = math.ceil(math.log2(N))
        deeps = [0]*(N)
        binaryParents = [[0]*M for i in range(N)]

        adj = [[] for i in range(N)]
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        # fill tables
        def dfs(id, parent, length):
            for nei in adj[id]:
                if nei == parent:
                    continue

                deeps[nei] = length+1
                binaryParents[nei][0] = id
                for j in range(1, M):
                    if binaryParents[nei][j-1] == 0:
                        break
                    binaryParents[nei][j] = binaryParents[binaryParents[nei][j-1]][j-1]
                    
                dfs(nei, id, length+1)

        dfs(1, 0, 0)

        # find lca
        def getLCA(node1, node2):
            if node1 == node2:
                return node1
            if deeps[node1] < deeps[node2]:
                node1, node2 = node2, node1
            diff = deeps[node1] - deeps[node2]

            for i in range(M-1, -1, -1):
                if (diff >> i) & 1 == 0:
                    continue

                if binaryParents[node1][i] == 0:
                    break
                node1 = binaryParents[node1][i]

            if node1 == node2:
                return node1

            for i in range(M-1, -1, -1):
                if binaryParents[node1][i] != binaryParents[node2][i]:
                    node1 = binaryParents[node1][i] 
                    node2 = binaryParents[node2][i]

            return binaryParents[node1][0]

        # multiply
        MOD = 10**9 + 7
        def getCount(degree):
            res = 1
            base = 2

            while degree > 0:
                if degree % 2 == 1:
                    res = res * base % MOD

                base = (base * base) % MOD
                degree = degree // 2

            return res

        res = [0]*len(queries)
        for i in range(len(queries)):
            s, e = queries[i]
            parent = getLCA(s, e)
            path = deeps[s]+deeps[e] - 2 * deeps[parent]

            # print('s', s, 'e', e, 'p', parent, 'path', path)
            
            if path < 2:
                res[i] = max(0, path)
                continue

            res[i] = getCount(path-1)
            
            


        return res

        
def test():
    params = [
        {
            "input": [[[1,2]], [[1,1],[1,2]]],
            "output": [0,1],
        },
        {
            "input": [[[1,2],[1,3],[3,4],[3,5]], [[1,4],[3,4],[2,5]]],
            "output": [2,1,4],
        },
    ]
    solution = Solution()

    for param in params:
        edges, queries = param["input"]
        result = solution.assignEdgeWeights(edges, queries)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
