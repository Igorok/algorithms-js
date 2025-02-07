from typing import List
import json
from collections import deque

class Solution:
    def queryResults_0(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballsWithColors = set()
        colorsWithBalls = set()
        n = len(queries)

        res = [0]*n
        for i in range(n):
            ball, color = queries[i]
            ballsWithColors.add(ball)
            colorsWithBalls.add(color)
            res[i] = min(len(ballsWithColors), len(colorsWithBalls))

        return res

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        if limit == 0:
            return []
        ballsWithColors = {}
        colorsWithBalls = {}
        colors = 0
        n = len(queries)

        res = [0]*n
        for i in range(n):
            b, c = queries[i]

            currentColor = ballsWithColors.get(b, 0)
            if currentColor != 0:
                count = colorsWithBalls.get(currentColor, 0)
                count -= 1
                colorsWithBalls[currentColor] = count
                if count == 0:
                    colors -= 1

            ballsWithColors[b] = c
            count = colorsWithBalls.get(c, 0)
            if count == 0:
                colors += 1
            colorsWithBalls[c] = count + 1

            res[i] = colors

        return res


def test ():
    params = [
        {
            'input': [4, [[1,4],[2,5],[1,3],[3,4]]],
            'output': [1,2,2,3],
        },
        {
            'input': [4, [[0,1],[1,2],[2,2],[3,4],[4,5]]],
            'output': [1,2,2,3,4],
        },
        {
            'input': [1, [[0,1],[0,4],[1,2],[1,5],[1,4]]],
            'output': [1,1,2,2,1],
        },
    ]
    solution = Solution()

    for param in params:
        limit, queries = param['input']
        result = solution.queryResults(limit, queries)
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
