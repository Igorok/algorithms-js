from typing import List
from json import dumps
from collections import deque

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 7 + 10**9
        memo = []
        for z in range(zero+2):
            memo.append([])
            for o in range(one+2):
                memo[z].append([-1]*2)


        def solve(z, o, last):
            nonlocal limit, MOD
            if z == 0 and o == 0:
                return 1

            if memo[z][o][last] != -1:
                return memo[z][o][last]

            res = 0

            if last == 1:
                available = min(z, limit)
                for i in range(1, available+1):
                    res = (res + solve(z-i, o, 0)) % MOD
            else:
                available = min(o, limit)
                for i in range(1, available+1):
                    res = (res + solve(z, o-i, 1)) % MOD

            memo[z][o][last] = res % MOD
            return memo[z][o][last]

        res = (solve(zero, one, 0) + solve(zero, one, 1)) % MOD

        memo = []



        return res



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
