from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def partitionString(self, s: str) -> int:
        aCode = ord('a')
        visited = [0]*26

        res = 0
        for char in s:
            code = ord(char) - aCode
            if visited[code] != 0:
                res += 1
                visited = [0]*26
            visited[code] += 1

        if sum(visited) != 0:
            res += 1

        return res

def test ():
    params = [
        {
            'input': 'abacaba',
            'output': 4,
        },
        {
            'input': 'ssssss',
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.partitionString(nums)
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
