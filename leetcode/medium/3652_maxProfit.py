from typing import List
import json
from collections import deque
import heapq
import math


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N = len(prices)
        prefixStrategy = [0] * N
        prefixPrice = [0] * N

        for i in range(N):
            prev = 0 if i == 0 else prefixStrategy[i-1]
            curr = prices[i] * strategy[i]
            prefixStrategy[i] = prev + curr

            prev = 0 if i == 0 else prefixPrice[i-1]
            prefixPrice[i] = prev + prices[i]

        half = k // 2
        res = prefixStrategy[-1]

        for left in range(N - k + 1):
            leftStrategySum = 0 if left == 0 else prefixStrategy[left-1]
            profitSum = prefixPrice[left + k - 1] - prefixPrice[left + half - 1]
            rightStrategySum = 0 if left + k == N else prefixStrategy[-1] - prefixStrategy[left + k - 1]

            r = leftStrategySum + profitSum + rightStrategySum

            res = max(res, r)

        return res

'''
[4,2,8], [-1,0,1], 2

-1,0,1 = -4 + 0 + 8 = 4
0 1 1 = 0 + 2 + 8 = 10
-1 0 1=


1,1,0
0 1 0
1 0 1

[[4,18,19,10], [0,-1,1,0], 2],

4,18,19,10
0 -18 19 0 = 1
0 -18 1 1
4 22 41 51

0,-1,1,0
0 1 1 0 = 0 + 18 + 19 + 0 = 37



'''


def test ():
    params = [
        {
            'input': [[4,2,8], [-1,0,1], 2],
            'output': 10,
        },
        {
            'input': [[5,4,3], [1,1,0], 2],
            'output': 9,
        },
        {
            'input': [[4,18,19,10], [0,-1,1,0], 2],
            'output': 37,
        },
    ]
    solution = Solution()

    for param in params:
        prices, strategy, k = param['input']
        result = solution.maxProfit(prices, strategy, k)
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
