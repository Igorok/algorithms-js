import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        combinations = set()
        used = [None]*n

        def rec(text: str):
            nonlocal combinations, used, tiles, n

            if len(text) == n:
                return

            for i in range(n):
                if used[i]:
                    continue
                newText = text + tiles[i]
                if newText in combinations:
                    continue

                used[i] = 1
                combinations.add(newText)
                rec(newText)
                used[i] = None

        rec('')

        return len(combinations)

'''
AAB
2 2 1 = 4
2 2 = 4
2 = 2


'''

def test ():
    params = [
        {
            'input': 'AAB',
            'output': 8,
        },
        {
            'input': 'AAABBC',
            'output': 188,
        },
        {
            'input': 'V',
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.numTilePossibilities(param['input'])
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
