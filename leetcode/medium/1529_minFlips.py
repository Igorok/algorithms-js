from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        res = 0
        updated = False

        for i in range(n-1, -1, -1):
            prev = target[i] if i == n-1 else target[i+1]
            if prev == target[i]:
                continue
            if target[i] == '0' and prev == '1':
                if res == 0:
                    res += 1
                continue
            if target[i] == '1' and prev == '0':
                res += 2


        return res

'''
10111

00000
  111

'''


def test ():
    params = [
        {
            'input': '001011101',
            'output': 5,
        },
        {
            'input': '10111',
            'output': 3,
        },
        {
            'input': '101',
            'output': 3,
        },
        {
            'input': '00000',
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        target = param['input']
        result = solution.minFlips(target)
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
