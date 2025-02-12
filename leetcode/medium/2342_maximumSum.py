import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maximumSum_0(self, nums: List[int]) -> int:
        n = len(nums)
        numsByDigits = defaultdict(list)

        def getDigitSum(num):
            r = 0
            while num != 0:
                r += num % 10
                num = num // 10
            return r

        for num in nums:
            s = getDigitSum(num)
            numsByDigits[s].append(num)

        res = -1

        for k in numsByDigits:
            if len(numsByDigits[k]) < 2:
                continue

            arr = sorted(numsByDigits[k])
            res = max(res, arr[-2]+arr[-1])


        return res

    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        numsByDigits = defaultdict(list)

        def getDigitSum(num):
            r = 0
            while num != 0:
                r += num % 10
                num = num // 10
            return r

        for num in nums:
            s = getDigitSum(num)
            numsByDigits[s].append(num)
            if len(numsByDigits[s]) > 2:
                numsByDigits[s] = sorted(numsByDigits[s])[1:]

        res = -1

        for k in numsByDigits:
            if len(numsByDigits[k]) < 2:
                continue

            res = max(res, sum(numsByDigits[k]))


        return res

def test ():
    params = [
        {
            'input': [18,43,36,13,7],
            'output': 54,
        },
        {
            'input': [10,12,19,14],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maximumSum(param['input'])
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
