from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def numberOfAlternatingGroups_0(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if k > n:
            return 0

        res = 0
        for i in range(n):
            isAlter = True
            for j in range(1, k):
                id = (n+i+j) % n
                prev = (n+i+j-1) % n
                if colors[id] == colors[prev]:
                    isAlter = False
                    break
            if isAlter:
                res += 1

        return res

    '''
    1 0 1 0 0 1 0 1 0 1
    + + + + -
            + + + + +
                + + + + +
                + + + + -
    1 0 0 1 1 0 1 0 1 1
    + + -
        + + -
            + + + + +
                + + + + -
    '''
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if k > n:
            return 0

        res = 0
        start = 0
        end = n + k - 1
        for i in range(1, end):
            id = i % n
            prev = (n + i - 1) % n

            if colors[id] == colors[prev]:
                start = i
            if i - start + 1 == k:
                res += 1
                start += 1

            if end - start < k:
                break

        return res


def test ():
    params = [
        {
            'input': [[0,1,0,1,0], 3],
            'output': 3,
        },
        {
            'input': [[0,1,0,0,1,0,1], 6],
            'output': 2,
        },
        {
            'input': [[1,1,0,1], 4],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        colors, k = param['input']
        result = solution.numberOfAlternatingGroups(colors, k)
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
