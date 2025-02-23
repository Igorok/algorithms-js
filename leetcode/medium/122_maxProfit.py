from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxProfit_0(self, prices: List[int]) -> int:
        expenses = [0]*len(prices)
        expenses[0] = prices[0]
        income = [0]*len(prices)

        for i in range(1, len(prices)):
            expenses[i] = min(expenses[i-1], prices[i], prices[i]-income[i-1])
            income[i] = max(income[i-1], prices[i] - expenses[i-1])
        return income[-1]

'''
7,1,5,3,6,4
7 1 1-1-1-3
0 0 4 4 7 7

expenses[i] = min(expenses[i-1], prices[i], prices[i]-income[i-1])
income[i] = max(income[i-1], prices[i] - expenses[i-1])

'''

def test ():
    params = [
        {
            'input': [7,1,5,3,6,4],
            'output': 7,
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

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
