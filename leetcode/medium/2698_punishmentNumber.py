from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def getSum(num: int, numStr: str, target: int):
            for i in range(1, len(numStr)):
                leftNum = int(numStr[:i])
                rightStr = numStr[i:]
                s = num + leftNum
                if s <= target and getSum(s, rightStr, target):
                    return True

            return num + int(numStr) == target

        def isCorrectNum(i):
            if i == 1:
                return True
            return getSum(0, str(i ** 2), i)

        s = 0
        for i in range(1, n+1):
            if isCorrectNum(i):
                s += i**2

        return s

'''

9
81

'''

def test ():
    params = [
        {
            'input': 10,
            'output': 182,
        },
        {
            'input': 37,
            'output': 1478,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.punishmentNumber(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
