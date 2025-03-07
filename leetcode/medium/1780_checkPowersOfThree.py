from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            r = n % 3
            if r == 2:
                return False
            n = n // 3

        return True


def test ():
    params = [
        {
            'input': 12,
            'output': True,
        },
        {
            'input': 91,
            'output': True,
        },
        {
            'input': 21,
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.checkPowersOfThree(n)
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
