from typing import List
import json
from collections import deque, defaultdict
from functools import cache


class Solution:
    def _getSquares(self, n):
        visited = [0]*(n+1)
        visited[1] = 1
        squares = set([1])

        for i in range(2, n+1):
            if visited[i] != 0:
                continue

            num = i**2
            while num < n+1:
                visited[num] = 1
                squares.add(num)
                num = num ** 2

        squares = sorted(list(squares), key = lambda x: -x)
        print('squares', squares)

        return squares

    def winnerSquareGame(self, n: int) -> bool:
        squares = self._getSquares(n)

        @cache
        def rec(remainder):
            for num in squares:
                if num > remainder:
                    continue

                r = rec(remainder-num)
                if not r:
                    return True


            return False



        return rec(n)

def test ():
    params = [
        {
            'input': 1,
            'output': True,
        },
        {
            'input': 2,
            'output': False,
        },
        {
            'input': 4,
            'output': True,
        },
        {
            'input': 10_000,
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.winnerSquareGame(n)
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
