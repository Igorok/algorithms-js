from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxProfit_0(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i1 in range(n):
            buy1 = prices[i1]
            for j1 in range(i1+1, n):
                if prices[j1] > prices[i1]:
                    profit1 = prices[j1] - prices[i1]

                    profit = max(profit, profit1)

                    for i2 in range(j1+1, n):
                        buy2 = prices[i2]
                        for j2 in range(i2+1, n):
                            if prices[j2] > prices[i2]:
                                profit2 = prices[j2] - prices[i2]

                                profit = max(profit, profit1+profit2)

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)

        maxRight = [0]*n
        righPprofit = [0]*n
        maxRight[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(prices[i], maxRight[i+1])
            righPprofit[i] = max(maxRight[i+1] - prices[i], righPprofit[i+1])

        minLeft = [0]*n
        leftPprofit = [0]*n
        minLeft[0] = prices[0]
        for i in range(1, n):
            minLeft[i] = min(minLeft[i-1], prices[i])
            leftPprofit[i] = max(leftPprofit[i-1], prices[i] - minLeft[i-1])

            res = max(res, leftPprofit[i])
            if i + 1 < n:
                res = max(res, leftPprofit[i] + righPprofit[i+1])

        return res

'''

3,3,5,0,0,3,1,4
max
5 5 5 4 4 4 4 4 -1
right profit
1 1 4 4 4 1 3 -5 0

min
3 3 3 0 0 0 0 0
left profit
0 0 2 2 2 3 1 4
'''

def test ():
    params = [
        {
            'input': [3,3,5,0,0,3,1,4],
            'output': 6,
        },
        {
            'input': [1,2,3,4,5],
            'output': 4,
        },
        {
            'input': [7,6,4,3,1],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxProfit(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
