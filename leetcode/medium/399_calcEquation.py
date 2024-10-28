from collections import deque
from typing import List
from json import dumps

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []

        nodes = {}
        for i in range(len(values)):
            s, e = equations[i]
            num = values[i]
            neiS = nodes.get(s, [])
            neiS.append((e, num))
            nodes[s] = neiS

            neiE = nodes.get(e, [])
            neiE.append((s, 1/num))
            nodes[e] = neiE

        def bfs(s, e):
            if not s in nodes or not e in nodes:
                return -1
            q = deque()
            visited = set()

            q.append((s, 1))
            while q:
                node, num = q.pop()
                for nei, n in nodes[node]:
                    if nei == e:
                        return n * num
                    if not nei in visited:
                        q.append((nei, num * n))
                        visited.add(nei)

            return -1

        res = []
        for s, e in queries:
            r = bfs(s, e)
            res.append(r)

        return res

'''
[["a","b"],["b","c"]],
[2.0,3.0],

[["a","b"],["b","c"]],
[2.0,3.0],
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

a/b = 2
b/c = 3
b = 3*c
b = 2*a
c = b/3

a/c=a/(b/3) = 3 a/b = 3 * 2

'''



def test ():
    params = [
        {
            'input': [
                [["a","b"],["b","c"]],
                [2.0,3.0],
                [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
            ],
            'output': [6.00000,0.50000,-1.00000,1.00000,-1.00000],
        },
        {
            'input': [
                [["a","b"],["b","c"],["bc","cd"]],
                [1.5,2.5,5.0],
                [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
            ],
            'output': [3.75000,0.40000,5.00000,0.20000],
        },
        {
            'input': [
                [["a","b"]],
                [0.5],
                [["a","b"],["b","a"],["a","c"],["x","y"]]
            ],
            'output': [0.50000,2.00000,-1.00000,-1.00000],
        },
    ]
    solution = Solution()

    for param in params:
        equations, values, queries = param['input']
        result = solution.calcEquation(equations, values, queries)

        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
