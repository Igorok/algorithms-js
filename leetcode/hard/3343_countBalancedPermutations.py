from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    mod = int(7 + 10e8)

    def modMul(self, a, b):
        return int((a % self.mod) * (b % self.mod) % self.mod)

    def generateFactorial(self, n):
        self.fact = [1] * (n+1)
        for i in range(1, n+1):
            self.fact[i] = self.modMul(self.fact[i-1], i)

    def binaryExponential(self, num, degree):
        res = 1
        while degree > 0:
            if degree & 1:
                res = self.modMul(res, num)
            num = self.modMul(num, num)
            degree >>= 1
        return res

    def generateInvertedFactorial(self, n):
        self.inversedFact = [1] * (n+1)
        for i in range(1, n+1):
            self.inversedFact[i] = self.binaryExponential(self.fact[i], self.mod - 2)

    def getCount(self, digit, leftover, target):
        if digit == 10:
            return self.allCombinations if (leftover == 0 and target == 0) else 0

        if self.memo[digit][leftover][target] != -1:
            return self.memo[digit][leftover][target]

        nextCount = min(leftover, self.freq[digit])
        if digit > 0:
            nextCount = min(nextCount, target // digit)

        res = 0
        for i in range(nextCount + 1):
            duplicates = self.modMul(self.inversedFact[i], self.inversedFact[self.freq[digit] - i])
            res += duplicates * self.getCount(digit+1, leftover-i, target - digit * i)
            res %= self.mod

        self.memo[digit][leftover][target] = res

        return res

    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        sumDigit = 0
        self.freq = [0]*10
        for char in num:
            digit = int(char)
            sumDigit += digit
            self.freq[digit] += 1

        if sumDigit % 2 == 1:
            return 0

        target = sumDigit // 2
        self.generateFactorial(n)
        self.generateInvertedFactorial(n)


        evenLength = n // 2
        self.allCombinations = self.modMul(self.fact[evenLength], self.fact[n - evenLength])

        maxSum = 41*9
        self.memo = [[[-1] * (maxSum + 1) for j in range(evenLength + 1)] for i in range(10)]


        return self.getCount(0, evenLength, target)


def test ():
    params = [
        {
            'input': '123',
            'output': 2,
        },
        {
            'input': '112',
            'output': 1,
        },
        {
            'input': '12345',
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        num = param['input']
        result = solution.countBalancedPermutations(num)
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
