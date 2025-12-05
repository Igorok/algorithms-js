from typing import List
import json
from collections import deque, defaultdict
import heapq
import math



class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        res = 0
        for char in directions:
            if char == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    res += 1
                stack.append(char)
            elif char == 'R':
                stack.append(char)
            elif char == 'L':
                if not stack:
                    continue
                elif stack[-1] == 'S':
                    res += 1
                elif stack[-1] == 'R':
                    res += 2
                    stack.pop()
                    while stack and stack[-1] == 'R':
                        stack.pop()
                        res += 1
                    stack.append('S')


        return res

'''
SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR
ssrssrllrsllrsrssrlrrrrllrrlssrr
1+2+1+1+1+1+1+1+2+2+1+2+1+1

'''

def test ():
    params = [
        {
            'input': 'SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR',
            'output': 20,
        },
        {
            'input': 'RLRSLL',
            'output': 5,
        },
        {
            'input': 'LLRR',
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        directions = param['input']
        result = solution.countCollisions(directions)
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
