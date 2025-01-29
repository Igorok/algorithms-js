from typing import List
import json
from collections import deque

class Solution:
    def checkIfPrerequisite_0(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = [[] for i in range(numCourses)]

        for s, e in prerequisites:
            parents[e].append(s)

        def dfs(start, end):
            def rec(e):
                r = False
                for p in parents[e]:
                    if p == start:
                        return True
                    r = r or rec(p)

                return r
            return rec(e)

        res = []
        for s, e in queries:
            res.append(dfs(s, e))

        return res

    def checkIfPrerequisite_1(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]
        income = [0]*numCourses
        visited = [set() for i in range(numCourses)]

        for s, e in prerequisites:
            income[e] += 1
            adj[s].append(e)

        def dfs(start, path):
            def rec(s, p):
                visited[s] = visited[s].union(p)
                p.add(s)
                for nei in adj[s]:
                    rec(nei, p.copy())

            rec(start, path)

        for i in range(numCourses):
            if income[i] == 0:
                dfs(i, set())

        res = []
        for s, e in queries:
            res.append(s in visited[e])

        return res


    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = [[] for i in range(numCourses)]
        visited = [set() for i in range(numCourses)]

        for s, e in prerequisites:
            parents[e].append(s)

        def dfs(start):
            def rec(s):
                for p in parents[s]:
                    if p in visited[start]:
                        continue
                    visited[start].add(p)
                    rec(p)

            rec(start)

        for i in range(numCourses):
            dfs(i)

        res = []
        for s, e in queries:
            res.append(s in visited[e])

        return res

'''

0 1 2 3
        7 8 9
4
5 6
    10 11


leaf -> root
income edges ?


'''



def test ():
    params = [
        {
            'input': [2, [[1,0]], [[0,1],[1,0]]],
            'output': [False, True],
        },
        {
            'input': [2, [], [[1,0],[0,1]]],
            'output': [False, False],
        },
        {
            'input': [3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]],
            'output': [True, True],
        },
        {
            'input': [4, [[2,3],[2,1],[0,3],[0,1]], [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]],
            'output': [True, True, True, False, False, False],
        },
        {
            'input': [
                7,
                [[2,3],[2,1],[2,0],[3,4],[3,6],[5,1],[5,0],[1,4],[1,0],[4,0],[0,6]],
                [[3,0],[6,4],[5,6],[2,6],[2,3],[5,6],[4,0],[2,6],[3,5],[5,3],[1,6],[1,0],[3,5],[6,5],[2,3],[3,0],[3,4],[3,4],[2,5],[0,3],[4,0],[6,4],[5,0],[6,5],[5,6],[6,5],[1,0],[3,4],[1,5],[1,4],[3,6],[0,1],[1,2],[5,1],[5,3],[5,3],[3,4],[5,4],[5,4],[5,3]]
            ],
            'output': [True, False, True, True, True, True, True, True, False, False, True, True, False, False, True, True, True, True, False, False, True, False, True, False, True, False, True, True, False, True, True, False, False, True, False, False, True, True, True, False],
        },

    ]
    solution = Solution()

    for param in params:
        numCourses, prerequisites, queries = param['input']
        result = solution.checkIfPrerequisite(numCourses, prerequisites, queries)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            '\n input', param['input'],
            '\n output', param['output'],
            '\n result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
