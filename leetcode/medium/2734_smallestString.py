from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache

class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        def getChar(char):
            if char == 'a':
                return 'z'
            return chr(ord(char) - 1)

        def changeChars(id):
            for j in range(id, -1, -1):
                if arr[j] == 'a':
                    break
                arr[j] = getChar(arr[j])

        changed = False
        arr = list(s)
        for i in range(0, n):
            if arr[i] == 'a' and i > 0 and arr[i-1] != 'a':
                changed = True
                changeChars(i-1)
                break

        if not changed:
            if arr[n-1] == 'a':
                arr[n-1] = getChar(arr[n-1])
            else:
                changeChars(n-1)


        return ''.join(arr)


def test ():
    params = [
        {
            'input': 'cbabc',
            'output': 'baabc',
        },
        {
            'input': 'aa',
            'output': 'az',
        },
        {
            'input': 'acbbc',
            'output': 'abaab',
        },
        {
            'input': 'aaaaaaa',
            'output': 'aaaaaaz',
        },
        {
            'input': 'b',
            'output': 'a',
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.smallestString(s)
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
