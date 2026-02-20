from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        N = len(arr)

        def dfs(id):
            if id == N:
                return N

            if id == -1:
                return -1

            if arr[id] == '':
                return -1

            if arr[id] == '#':
                return id + 1

            fromLeft = dfs(id+1)
            if fromLeft == N:
                return -1
            fromRight = dfs(fromLeft)

            return fromRight



        return True if dfs(0) == N else False


def test ():
    params = [
        {
            'input': "9,3,4,#,#,1,#,#,2,#,6,#,#",
            'output': True,
        },
        {
            'input': "1,#",
            'output': False,
        },
        {
            'input': "9,#,#,1",
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        preorder = param['input']
        result = solution.isValidSerialization(preorder)
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
