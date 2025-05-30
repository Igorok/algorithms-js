from typing import List
import json
from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        childCount = [0] * n
        parents = [[] for i in range(n)]
        colorsByNodes = [[0]*26 for i in range(n)]

        for s, e in edges:
            childCount[s] += 1
            parents[e].append(s)

        nodesQueue = deque()
        for i in range(n):
            nodeColor = ord(colors[i]) - ord('a')
            colorsByNodes[i][nodeColor] = 1

            if childCount[i] == 0:
                nodesQueue.append(i)

        res = 1
        while nodesQueue:
            node = nodesQueue.popleft()
            for p in parents[node]:
                childCount[p] -= 1

                parentColor = ord(colors[p]) - ord('a')

                for c in range(26):
                    countColors = colorsByNodes[node][c] + 1 if parentColor == c else colorsByNodes[node][c]
                    colorsByNodes[p][c] = max(colorsByNodes[p][c], countColors)

                if childCount[p] == 0:
                    nodesQueue.append(p)
                    res = max(res, max(colorsByNodes[p]))



        if sum(childCount) != 0:
            return -1

        return res



def test ():
    params = [
        {
            'input': ["g", []],
            'output': 1,
        },
        {
            'input': ["abaca", [[0,1],[0,2],[2,3],[3,4]]],
            'output': 3,
        },
        {
            'input': ["a", [[0,0]]],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        colors, edges = param['input']

        result = solution.largestPathValue(colors, edges)
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
