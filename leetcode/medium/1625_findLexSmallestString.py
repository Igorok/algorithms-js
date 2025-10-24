from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        pivot = n - b
        cache = {}

        def dfs(text: str) -> str:
            if text in cache:
                return cache[text]

            cache[text] = text

            r = dfs(text[pivot:] + text[:pivot])
            if r < cache[text]:
                cache[text] = r

            arr = list(text)
            for i in range(1, n, 2):
                arr[i] = str((int(arr[i]) + a) % 10)

            arr = arr[pivot:] + arr[:pivot]
            arr = ''.join(arr)

            if arr < cache[text]:
                cache[text] = arr

            r = dfs(arr)
            if r < cache[text]:
                cache[text] = r

            return cache[text]

        return dfs(s)


def test ():
    params = [
        {
            'input': ["5525", 9, 2],
            'output': '2050',
        },
        {
            'input': ["74", 5, 1],
            'output': '24',
        },
        {
            'input': ["0011", 4, 2],
            'output': '0011',
        },
    ]
    solution = Solution()

    for param in params:
        s, a, b = param['input']
        result = solution.findLexSmallestString(s, a, b)
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
