from typing import List
import heapq

class Solution_0:
    def numOfWays(self, n: int) -> int:
        MOD = 7 + 10**9

        memo = []
        for r in range(n):
            row = [[0]*3 for i in range(3)]
            memo.append(row)

        for r in range(n):
            for c in range(3):
                # red
                top = 1 if r == 0 else (memo[r-1][c][1] + memo[r-1][c][2]) % MOD
                left = 1 if c == 0 else (memo[r][c-1][1] + memo[r][c-1][2]) % MOD
                diag = 1 if r == 0 or c == 0 else (memo[r-1][c-1][1] + memo[r-1][c-1][2]) % MOD
                memo[r][c][0] = (top * left / diag) % MOD

                # green
                top = 1 if r == 0 else (memo[r-1][c][0] + memo[r-1][c][2]) % MOD
                left = 1 if c == 0 else (memo[r][c-1][0] + memo[r][c-1][2]) % MOD
                diag = 1 if r == 0 or c == 0 else (memo[r-1][c-1][0] + memo[r-1][c-1][2]) % MOD
                memo[r][c][1] = (top * left / diag) % MOD

                # yellow
                top = 1 if r == 0 else (memo[r-1][c][0] + memo[r-1][c][1]) % MOD
                left = 1 if c == 0 else (memo[r][c-1][0] + memo[r][c-1][1]) % MOD
                diag = 1 if r == 0 or c == 0 else (memo[r-1][c-1][0] + memo[r-1][c-1][1]) % MOD
                memo[r][c][2] = (top * left / diag) % MOD

        print(memo)

        return (memo[-1][-1][0] + memo[-1][-1][1] + memo[-1][-1][2]) % MOD


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 7 + 10**9

        abc = 6
        aba = 6

        for i in range(1, n):
            next_abc = (2*abc%MOD + 2*aba%MOD) % MOD
            next_aba = (2*abc%MOD + 3*aba%MOD) % MOD

            abc = next_abc
            aba = next_aba

        return (abc+aba) % MOD

'''

RGY = 3*2*1 = 6
RGR = 3*2 = 6
0: 6+6=12

RGY:
    RGY: GYR, YRG
    RGR: GRG, GYG
RGR:
    RGY: GRY, YRG
    RGR: YRY, GYG, GRG



'''


def test ():
    params = [
        {
            'input': 1,
            'output': 12,
        },
        {
            'input': 2,
            'output': 54,
        },
        {
            'input': 3,
            'output': 246,
        },
        {
            'input': 5000,
            'output': 30228214,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.numOfWays(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
