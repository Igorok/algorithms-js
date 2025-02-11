from typing import List
import json
from collections import deque

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isnumeric():
                if len(stack) and not stack[-1].isnumeric():
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return ''.join(stack)

def test ():
    params = [
        {
            'input': 'abc',
            'output': 'abc',
        },
        {
            'input': 'cb34',
            'output': '',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.clearDigits(param['input'])
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
