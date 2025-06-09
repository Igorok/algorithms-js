import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        charsQueue = []

        for i in range(n):
            char = s[i]
            if char == '*' and charsQueue:
                heapq.heappop(charsQueue)
            else:
                heapq.heappush(charsQueue, (ord(char), -i))

        charsQueue.sort(key=lambda x: abs(x[1]))
        charsQueue = [chr(char) for char, i in charsQueue]

        return ''.join(charsQueue)

def test ():
    params = [
        {
            'input': "aaba*",
            'output': "aab",
        },
        {
            'input': "abc",
            'output': "abc",
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.clearStars(param['input'])
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
