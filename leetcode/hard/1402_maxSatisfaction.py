from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def maxSatisfaction_0(self, satisfaction: List[int]) -> int:
        dishes = sorted(satisfaction)
        if dishes[-1] <= 0:
            return 0

        bareSum = 0
        multiplySum = 0

        for i in range(len(dishes) - 1, -1, -1):
            satis = dishes[i]
            coeff = (i+1) * satis

            if multiplySum - bareSum > multiplySum + coeff:
                multiplySum -= bareSum
            else:
                multiplySum += coeff
                bareSum += satis

        return multiplySum

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        positive = []
        negative = []
        posSum = 0
        for num in satisfaction:
            if num < 0:
                negative.append(num)
            else:
                posSum += num
                positive.append(num)

        if posSum == 0:
            return 0

        positive.sort()
        negative.sort(key=lambda x: -x)

        totalPos = 0
        posSum = 0
        for i in range(len(positive)):
            posSum += positive[i]
            totalPos += (i+1) * positive[i]

        totalSum = totalPos
        totalNegative = 0
        negSum = 0
        for num in negative:
            negSum += num
            totalNegative += negSum
            totalPos += posSum

            if totalPos + totalNegative >= totalSum:
                totalSum = totalPos + totalNegative
            else:
                break

        return totalSum
'''

[-2,5,-1,0,3,-3]
-1 -2 -3
0 3 5


0 6 15

-1 0 9 20 = 28
-2 -2 0 12 25 = 37 - 4 = 33
-3 - 4 -3 0 15 30 = 45 - 10 = 35



'''

def test ():
    params = [
        {
            'input': [-2,5,-1,0,3,-3],
            'output': 35,
        },


        {
            'input': [-1,-8,0,5,-9],
            'output': 14,
        },
        {
            'input': [4,3,2],
            'output': 20,
        },
        {
            'input': [-1,-4,-5],
            'output': 0,
        },
        {
            'input': [2,-2,-3,1],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxSatisfaction(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
