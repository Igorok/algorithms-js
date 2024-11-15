from typing import List
from json import dumps
import heapq

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)

        payed = [0] * l
        payed[0] = cost[0]
        payed[1] = cost[1]

        for i in range(2, l):
            payed[i] = min(payed[i-1], payed[i-2]) + cost[i]

        print('payed', payed)

        return min(payed[l-1], payed[l-2])

def test ():
    params = [
        {
            'input': [10,15,20],
            'output': 15,
        },
        {
            'input': [1,100,1,1,1,100,1,1,100,1],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minCostClimbingStairs(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
