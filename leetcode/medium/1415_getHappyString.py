from typing import List
import json
from collections import deque

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ('a', 'b', 'c')
        used = set()

        q = deque()

        for char in chars:
            q.append(char)

        count = 0
        while q:
            text = q.popleft()
            if len(text) == n:
                count += 1
                if count == k:
                    return text
                continue

            for char in chars:
                if char == text[-1]:
                    continue
                q.append(text + char)


        return ''

def test ():
    params = [
        {
            'input': [1, 3],
            'output': 'c',
        },
        {
            'input': [1, 4],
            'output': '',
        },
        {
            'input': [3, 9],
            'output': 'cab',
        },
    ]
    solution = Solution()

    for param in params:
        n, k = param['input']
        result = solution.getHappyString(n, k)
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
