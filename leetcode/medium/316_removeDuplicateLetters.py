import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution_0:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        count = defaultdict(int)
        smallest = ['z']*n
        smallest[n-1] = s[-1]
        count[s[n-1]] = 1

        for i in range(n-2, -1, -1):
            count[s[i]] += 1
            smallest[i] = smallest[i+1] if smallest[i+1] < s[i] else s[i]

        res = []
        for i in range(n):
            char = s[i]
            count[char] -= 1

            if count[char] == 0:
                res.append(char)
                continue

            if smallest[i] <= s[i]:
                continue

        return ''.join(res)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        count = defaultdict(int)

        for i in range(n):
            count[s[i]] += 1

        stack = []
        used = set()
        for i in range(n):
            char  = s[i]
            count[char] -= 1
            if char in used:
                continue

            while len(stack) > 0 and stack[-1] > char and count[stack[-1]] > 0:
                prev = stack.pop()
                used.remove(prev)

            stack.append(char)
            used.add(char)



        return ''.join(stack)

'''
abcdabcd

'''

def test ():
    params = [
        {
            'input': "bcabc",
            'output': 'abc',
        },
        {
            'input': "cbacdcbc",
            'output': 'acdb',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.removeDuplicateLetters(param['input'])
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
