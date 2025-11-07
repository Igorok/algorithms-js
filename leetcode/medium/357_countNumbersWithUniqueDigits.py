from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cache = {}

        def dfs(id, acc, isEmpty):
            key = f"{ id }_{ '_'.join([str(n) for n in acc]) }_{ isEmpty }"

            if key in cache:
                return cache[key]

            if id == n:
                return 1

            cache[key] = 0

            for i in range(10):
                if not isEmpty and acc[i] == 1:
                    continue

                isE = isEmpty and i == 0
                if not isE:
                    acc[i] = 1

                cache[key] += dfs(id + 1, acc, isE)
                acc[i] = 0

            return cache[key]

        return dfs(0, [0]*11, True)


def test ():
    params = [
        {
            'input': 2,
            'output': 91,
        },
        {
            'input': 0,
            'output': 1,
        },
        {
            'input': 8,
            'output': 2345851,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.countNumbersWithUniqueDigits(n)
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
