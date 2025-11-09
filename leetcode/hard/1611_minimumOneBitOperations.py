from typing import List
import json
from collections import deque, defaultdict
import math

class Solution_0:
    def minimumOneBitOperations(self, n: int) -> int:
        arr = list(bin(n)[2:])
        n = len(arr)
        cache = {}

        def dfs(arr):
            key = ''.join(arr)
            if key in cache:
                return cache[key]

            cache[key] = float('inf')

            first = -1
            second = -1
            last = -1

            for i in range(n):
                if arr[i] == '1':
                    if first == -1:
                        first = i
                        continue
                    if second == -1:
                        second = i
                        continue
                    last = i


            if first == -1:
                return 0

            if first == n-1:
                return 1

            if second == -1:
                data = arr.copy()
                data[n-1] = '1'
                cache[key] = min(cache[key], 1 + dfs(data))
                return cache[key]

            if last == -1:
                if first - second == 1:
                    data = arr.copy()
                    data[first] = '0'
                    cache[key] = min(cache[key], 1 + dfs(data))
                    return cache[key]
                else:
                    data = arr.copy()
                    data[second - 1] = '0' if data[second - 1] == '1' else '1'
                    cache[key] = min(cache[key], 1 + dfs(data))

                    data = arr.copy()
                    data[n-1] = '0' if data[n-1] == '1' else '1'
                    cache[key] = min(cache[key], 1 + dfs(data))
                    return cache[key]

            data = arr.copy()
            data[last-1] = '0' if data[last-1] == '1' else '1'
            cache[key] = min(cache[key], 1 + dfs(data))

            data = arr.copy()
            data[n-1] = '0' if data[n-1] == '1' else '1'
            cache[key] = min(cache[key], 1 + dfs(data))


            return cache[key]

        return dfs(arr)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def dfs(num):
            if num == 0:
                return 0

            num1 = num
            i = 0
            power = 0
            while num1 != 0:
                if num1 & 1 == 1:
                    power = i

                num1 = num1 >> 1
                i += 1

            res = 2 ** (power + 1) - 1
            res -= dfs(num ^ (2 ** power))

            return res

        return dfs(n)





'''
0100
0101
0111
0110
0010
0011
0001
0000

01000
01001
01011
01010
01110
01111
01101
01100
00100
00101
00111
00110
00010
00011
00001
00000



https://en.wikipedia.org/wiki/Gray_code

'''


def test ():
    params = [
        {
            'input': 4,
            'output': 7,
        },
        {
            'input': 3,
            'output': 2,
        },
        {
            'input': 6,
            'output': 4,
        },
        {
            'input': 8,
            'output': 15,
        },
        {
            'input': 800,
            'output': 575,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.minimumOneBitOperations(s)
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
