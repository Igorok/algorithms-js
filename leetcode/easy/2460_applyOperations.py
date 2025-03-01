from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        n = len(arr)
        res = []
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                arr[i] *= 2
                arr[i+1] = 0

            if arr[i] != 0:
                res.append(arr[i])

        if arr[-1] != 0:
            res.append(arr[-1])

        for i in range(len(res), n):
            res.append(0)

        return res

'''
1,2,2,1,1,0
1 4 0 1

'''


def test ():
    params = [
        {
            'input': [1,2,2,1,1,0],
            'output': [1,4,2,0,0,0],
        },
        {
            'input': [0,1],
            'output': [1,0],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.applyOperations(param['input'])
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
