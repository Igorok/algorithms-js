from typing import List
from json import dumps
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        income = [0]*numCourses

        for e, s in prerequisites:
            adj[s].append(e)
            income[e] += 1

        vertexQueue = deque()
        for i in range(len(income)):
            if income[i] == 0:
                vertexQueue.append(i)

        completed = 0

        while vertexQueue:
            node = vertexQueue.pop()
            for nei in adj[node]:
                income[nei] -= 1
                if income[nei] == 0:
                    vertexQueue.append(nei)
            completed += 1


        return completed == numCourses


def test ():
    params = [
        {
            'input': [2, [[1,0]]],
            'output': True,
        },
        {
            'input': [2, [[1,0],[0,1]]],
            'output': False,
        },
        {
            'input': [3, [[1,0],[2,0]]],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        numCourses, prerequisites = param['input']

        result = solution.canFinish(numCourses, prerequisites)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
