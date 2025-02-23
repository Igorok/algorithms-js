from typing import List
import json
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        incomes = [0]*numCourses

        for a, b in prerequisites:
            adj[a].append(b)
            incomes[b] += 1

        nodesQueue = deque()
        for i in range(numCourses):
            if incomes[i] == 0:
                nodesQueue.append(i)

        res = []
        while nodesQueue:
            node = nodesQueue.pop()
            res.append(node)

            for nei in adj[node]:
                incomes[nei] -= 1
                if incomes[nei] == 0:
                    nodesQueue.append(nei)
        res.reverse()

        return res if len(res) == numCourses else []

'''

[4, [[1,0],[2,0],[3,1],[3,2]]]

3 1 0
3 2 0

'''


def test ():
    params = [
        {
            'input': [2, [[1,0]]],
            'output': [0,1],
        },
        {
            'input': [4, [[1,0],[2,0],[3,1],[3,2]]],
            'output': [0,2,1,3],
        },
        {
            'input': [1, []],
            'output': [0],
        },
    ]
    solution = Solution()

    for param in params:
        numCourses, prerequisites = param['input']
        result = solution.findOrder(numCourses, prerequisites)
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
