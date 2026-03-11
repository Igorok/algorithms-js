from typing import List
from json import dumps
from collections import deque

class Solution_0_0:
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
                # if val == 0:
                for l in range(1, limit+1):
                    prevOne = o - l
                    if prevOne < 0:
                        break
                    memo[0][z][o] = (memo[0][z][o] + memo[1][z][prevOne]) % MOD
                # val == 1
                for l in range(1, limit+1):
                    prevZero = z - l
                    if prevZero < 0:
                        break
                    memo[1][z][o] = (memo[1][z][o] + memo[0][prevZero][o]) % MOD


        # print(memo)

        return (memo[0][zero][one] + memo[1][zero][one]) % MOD

class Solution_0:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 7 + 10**9

        memo = [
            [], # ended by 0
            [], # ended by 1
        ]
        for i in range(2):
            for z in range(zero+1):
                memo[i].append([0]*(one+1))

        # fill only 0
        for z in range(min(limit, zero)+1):
            memo[0][z][0] = 1

        # fill only 1
        for o in range(min(limit, one)+1):
            memo[1][0][o] = 1

        print(memo)

        for z in range(1, zero+1):
            for o in range(1, one+1):
                # we want to add 0
                # add all values with zero from 1 to limit and ended by 1
                for l in range(1, limit+1):
                    prevZero = z - l
                    if prevZero < 0:
                        break
                    memo[0][z][o] = (memo[0][z][o] + memo[1][prevZero][o]) % MOD
                # we want to add 1
                # add all values with one from 1 to limit and ended by 0
                for l in range(1, limit+1):
                    prevOne = o - l
                    if prevOne < 0:
                        break
                    memo[1][z][o] = (memo[1][z][o] + memo[0][z][prevOne]) % MOD


        # print(memo)

        return (memo[0][zero][one] + memo[1][zero][one]) % MOD


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 7 + 10**9

        memo = [
            [], # ending by 0
            [], # ending by 1
        ]
        for i in range(2):
            for z in range(zero+1):
                memo[i].append([0]*(one+1))

        # ending by 0
        for z in range(min(limit, zero)+1):
            memo[0][z][0] = 1

        # ending by 1
        for o in range(min(limit, one)+1):
            memo[1][0][o] = 1

        # print(memo)

        for z in range(1, zero+1):
            for o in range(1, one+1):
                # we want add 0
                # we accamulate all memo[0][z-1][o] + memo[1][z-1][o]
                # but all values with 1 before limit invalid
                # memo[0][z][o] -= memo[1][z-1-limit][o]
                memo[0][z][o] = (memo[0][z-1][o] + memo[1][z-1][o]) % MOD
                if z > limit:
                    memo[0][z][o] = (MOD + memo[0][z][o] - memo[1][z-1-limit][o]) % MOD

                # we want add 1
                # we accamulate all from memo[0][z][o-1] + all memo[0][z][o1]
                # but all values ended by 0 before limit invalid
                # memo[1][z][o] - memo[0][z][o-1-limit]
                memo[1][z][o] = (memo[1][z][o-1] + memo[0][z][o-1]) % MOD
                if o > limit:
                    memo[1][z][o] = (MOD + memo[1][z][o] - memo[0][z][o-1-limit]) % MOD


        # print(memo)

        return (memo[0][zero][one] + memo[1][zero][one]) % MOD


class Solution_2:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # dp[0][i][j] = number of stable arrays with i zeros, j ones, ending in 0
        # dp[1][i][j] = number of stable arrays with i zeros, j ones, ending in 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # --- Base Cases ---
        # If we only have zeros, there is exactly 1 stable way if zeros <= limit
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        # If we only have ones, there is exactly 1 stable way if ones <= limit
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        # --- DP Transitions ---
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # To end in 0: we can add a '0' to any stable array ending in 0 or 1
                # that has i-1 zeros and j ones.
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i > limit:
                    # Subtract cases where we'd have limit+1 zeros.
                    # This happens if we add a '0' to a sequence that ended in '1'
                    # followed by exactly 'limit' zeros.
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD

                # To end in 1: we can add a '1' to any stable array ending in 0 or 1
                # that has i zeros and j-1 ones.
                dp1[i][j] = (dp1[i][j-1] + dp0[i][j-1]) % MOD
                if j > limit:
                    # Subtract cases where we'd have limit+1 ones.
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD


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
        {
            'input': [1,1,1],
            'output': 2,
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
