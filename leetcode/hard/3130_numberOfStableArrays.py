from typing import List
from json import dumps
from collections import deque

class Solution_0:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 7 + 10**9

        memo = [[], []]
        for i in range(2):
            for z in range(zero+1):
                memo[i].append([0]*(one+1))

        for o in range(min(limit, one)+1):
            memo[0][0][o] = 1
        for z in range(min(limit, zero)+1):
            memo[1][z][0] = 1

        # print(memo)

        for z in range(1, zero+1):
            for o in range(1, one+1):
                for val in range(2):
                    if val == 0:
                        for l in range(1, limit+1):
                            prevOne = o - l
                            if prevOne < 0:
                                break
                            memo[0][z][o] = (memo[0][z][o] + memo[1][z][prevOne]) % MOD
                    else:
                        for l in range(1, limit+1):
                            prevZero = z - l
                            if prevZero < 0:
                                break
                            memo[1][z][o] = (memo[1][z][o] + memo[0][prevZero][o]) % MOD


        # print(memo)

        return (memo[0][zero][one] + memo[1][zero][one]) % MOD


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 7 + 10**9

        memo = [[], []]
        for i in range(2):
            for z in range(zero+1):
                memo[i].append([0]*(one+1))

        for o in range(1, min(limit, one)+1):
            memo[0][0][o] = 1
        for z in range(1, min(limit, zero)+1):
            memo[1][z][0] = 1

        # print(memo)

        for z in range(1, zero+1):
            for o in range(1, one+1):
                # 0
                memo[0][z][o] = (memo[0][z-1][o] + memo[1][z-1][o]) % MOD
                if z-1-limit >= 0:
                    memo[0][z][o] = (MOD + memo[0][z][o] - memo[1][z-1-limit][o]) % MOD
                # 1
                memo[1][z][o] = (memo[1][z][o-1] + memo[0][z][o-1]) % MOD
                if o-1-limit >= 0:
                    memo[1][z][o] = (MOD + memo[1][z][o] - memo[0][z][o-1-limit]) % MOD



        # print(memo)

        return (memo[0][zero][one] + memo[1][zero][one]) % MOD

'''

[[[1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]]
[[[1, 1, 1, 0], [0, 1, 2, 2], [0, 1, 3, 5], [0, 0, 2, 7]], [[1, 0, 0, 0], [1, 1, 1, 0], [1, 2, 3, 2], [0, 2, 5, 7]]]


'''


def test ():
    params = [
        {
            'input': [1, 1, 2],
            'output': 2,
        },
        {
            'input': [1, 2, 1],
            'output': 1,
        },
        {
            'input': [3, 3, 2],
            'output': 14,
        },
        {
            'input': [1,4,1],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        zero, one, limit = param['input']
        result = solution.numberOfStableArrays(zero, one, limit)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
