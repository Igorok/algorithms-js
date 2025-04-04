from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = [-1]*n

        def getNextScore(i):
            nonlocal n, cache, questions
            if i >= n:
                return 0

            if cache[i] != -1:
                return cache[i]

            r1 = 0
            r2 = 0

            r1 = questions[i][0] + getNextScore(i + questions[i][1] + 1)

            j = i + 1
            if j < n:
                r2 = getNextScore(j)

            cache[i] = max(r1, r2)
            return cache[i]


        return getNextScore(0)

def test ():
    params = [
        {
            'input': [[12,46],[78,19],[63,15],[79,62],[13,10]],
            'output': 79,
        },
        {
            'input': [[3,2],[4,3],[4,4],[2,5]],
            'output': 5,
        },
        {
            'input': [[1,1],[2,2],[3,3],[4,4],[5,5]],
            'output': 7,
        },
    ]
    solution = Solution()

    for param in params:
        questions = param['input']
        result = solution.mostPoints(questions)
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
