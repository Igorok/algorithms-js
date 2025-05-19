from typing import List
import json
from collections import deque


class Solution_0:
    MOD = 10**9 + 7

    def __init__(self):
        self.state_mem = [[-1] * 1024 for _ in range(1002)]  # 1000 rows + 2, 1024 for 10 bits

    def colorTheGrid(self, m: int, n: int) -> int:
        return self.countWays(m, n, 0, 0, 0, 0)

    def countWays(self, m, n, r, c, curr_state, prev_state):
        if c == n:
            return 1
        if r == m:
            return self.countWays(m, n, 0, c + 1, 0, curr_state)
        if r == 0 and self.state_mem[c][prev_state] != -1:
            return self.state_mem[c][prev_state]

        up_color = 0
        if r > 0:
            up_color = curr_state & 3

        left_color = (prev_state >> ((m - r - 1) * 2)) & 3

        ways_to_color = 0
        for color in range(1, 4):
            if color != up_color and color != left_color:
                new_state = (curr_state << 2) | color
                ways_to_color = (ways_to_color + self.countWays(m, n, r + 1, c, new_state, prev_state)) % self.MOD

        if r == 0:
            self.state_mem[c][prev_state] = ways_to_color
        return ways_to_color


'''
00 - white
01 -red
10 - green
11 - blue

5 * 2 bit = 10 bit
1 << 10 = 1024

m = 5
n = 1000
'''
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 7 + 10**9
        memo = [[-1]*(1<<10) for i in range(1001)]

        def rec(row, column, prev, curr):
            nonlocal m, n, memo, mod

            if row == n:
                return 1
            if column == m:
                return rec(row + 1, 0, curr, 0)
            if column == 0 and memo[row][prev] != -1:
                return memo[row][prev]

            leftVal = curr & 3
            shift = (m - column - 1) * 2
            topVal = (prev >> shift) & 3

            res = 0
            for color in range(1, 4):
                if color != leftVal and color != topVal:
                    updated = (curr << 2) | color
                    res += rec(row, column + 1, prev, updated)
                    res %= mod

            if column == 0:
                memo[row][prev] = res

            return res

        return rec(0, 0, 0, 0)



def test ():
    params = [
        {
            'input': [1, 1],
            'output': 3,
        },
        {
            'input': [1, 2],
            'output': 6,
        },
        {
            'input': [5, 5],
            'output': 580986,
        },
        {
            'input': [2, 37],
            'output': 478020091,
        },
    ]
    solution = Solution()

    for param in params:
        m, n = param['input']
        result = solution.colorTheGrid(m, n)
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
