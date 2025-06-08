import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        current = 0
        point = 1
        step = 0

        while point + step < n:
            if s[current + step] == s[point + step]:
                step += 1
            elif s[current + step] > s[point + step]:
                point = point + step + 1
                step = 0
            else:
                current, point = point, max(point + 1, current + step + 1)
                step = 0


        return s[current:]

'''

cacacacacacb
  cacacacacb
    cacacacb
      cacacb
        cacb
          cb

caaabcaaabcd
     caaabc

'''


def test ():
    params = [
        {
            'input': 'cccccd',
            'output': 'd',
        },
        {
            'input': 'dcbadcbadcbadcbb',
            'output': 'dcbb',
        },
        {
            'input': 'cacacb',
            'output': 'cb',
        },
        {
            'input': 'abab',
            'output': 'bab',
        },
        {
            'input': 'leetcode',
            'output': 'tcode',
        },
        {
            'input': 'vmjtxddvzmwrjvfamgpoowncslddrkjhchqswkamnsitrcmnhn',
            'output': 'zmwrjvfamgpoowncslddrkjhchqswkamnsitrcmnhn',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.lastSubstring(param['input'])
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
