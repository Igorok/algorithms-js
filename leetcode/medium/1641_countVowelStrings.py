from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq


class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        m = len(vowels)
        cache = {}
        def rec(id, charId):
            if (id, charId) in cache:
                return cache[(id, charId)]

            if id == n:
                return 1
            if charId == m:
                return 0

            r = 0
            for i in range(charId, m):
                r += rec(id + 1, i)

            cache[(id, charId)] = r

            return r

        return rec(0, 0)

def test ():
    params = [
        {
            'input': 1,
            'output': 5,
        },
        {
            'input': 2,
            'output': 15,
        },
        {
            'input': 33,
            'output': 66045,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.countVowelStrings(n)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
