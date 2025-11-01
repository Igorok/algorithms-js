from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            if not stack:
                if char != '0':
                    stack.append(char)
                continue

            while stack and k > 0 and char < stack[-1]:
                stack.pop()
                k -= 1

            if not stack and char == '0':
                continue
            else:
                stack.append(char)

        if k == 0:
            return '0' if not stack else ''.join(stack)

        length = len(stack)
        if k >= length:
            return '0'

        stack = stack[:length-k]

        return ''.join(stack)



'''
3
1 2 3 4

'''


def test ():
    params = [
        {
            'input': ["112", 1],
            'output': '11',
        },
        {
            'input': ["999", 3],
            'output': '0',
        },
        {
            'input': ["9", 1],
            'output': '0',
        },
        {
            'input': ["1432219", 3],
            'output': '1219',
        },
        {
            'input': ["10200", 1],
            'output': '200',
        },
        {
            'input': ["10", 2],
            'output': '0',
        },
    ]
    solution = Solution()

    for param in params:
        num, k = param['input']
        result = solution.removeKdigits(num, k)
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
