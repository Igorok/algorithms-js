import heapq
from collections import defaultdict
from functools import cache
from json import dumps
from typing import List

"""
Hello do you know leetcode issue = "3558. Number of Ways to Assign Edge Weights I"?
I implement intuition and it is wokirng:

```
1 step
odd = 1
even = 1
2 step
odd = (prevOddCount, because +2 ) + (prevEvenCount, because +1)
even = (prevOddCount, because +1 ) + (prevEvenCount, because +2)
3 step
odd = (prevOddCount, because +2 ) + (prevEvenCount, because +1)
even = (prevOddCount, because +1 ) + (prevEvenCount, because +2)
```

It is looking stupid, but I'm not sure about optimization, is it just 2^(maxLength)?
```
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        N = len(edges) + 2
        adj = [[] for i in range(N)]

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def dfs(node, parent):
            res = [0, 0, 0]

            for nei in adj[node]:
                if nei == parent:
                    continue
                r = dfs(nei, node)
                if r[2] > res[2]:
                    res = r

            if res[2] == 0:
                return [0, 0, 1]

            if res[2] == 1:
                return [1, 1, 2]

            length = res[2]
            even = (res[0] + res[1]) % MOD
            odd = (res[1] + res[0]) % MOD

            return [even, odd, length + 1]

        res = dfs(1, 1)

        return res[1]
```

"""


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        N = len(edges) + 2
        adj = [[] for i in range(N)]

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def dfs(node, parent):
            res = [0, 0, 0]

            for nei in adj[node]:
                if nei == parent:
                    continue
                r = dfs(nei, node)
                if r[2] > res[2]:
                    res = r

            if res[2] == 0:
                return [0, 0, 1]

            if res[2] == 1:
                return [1, 1, 2]

            length = res[2]
            even = (res[0] + res[1]) % MOD
            odd = (res[1] + res[0]) % MOD

            return [even, odd, length + 1]

        res = dfs(1, 1)

        return res[1]


def test():
    params = [
        {
            "input": [[1, 2]],
            "output": 1,
        },
        {
            "input": [[1, 2], [1, 3], [3, 4], [3, 5]],
            "output": 2,
        },
        {
            "input": [[3, 2], [2, 1]],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        edges = param["input"]
        result = solution.assignEdgeWeights(edges)
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
