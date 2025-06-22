from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    MOD = 7 + 10**9
    fact = []
    invFact = []

    def binExp(self, num, exp):
        res = 1
        num %= self.MOD

        while exp > 0:
            if exp & 1:
                res = (res * num) % self.MOD

            num = (num * num) % self.MOD
            exp = exp >> 1

        return res

    def mmi(self, num):
        return self.binExp(num, self.MOD - 2)

    def factorial(self, length):
        self.fact = [1] * (length+1)
        for i in range(1, length + 1):
            self.fact[i] = (self.fact[i-1] * i) % self.MOD

    def inverseFactorial(self, length):
        self.invFact = [1]*(length + 1)
        self.invFact[length] = self.mmi(self.fact[length])
        for i in range(length, -1, -1):
            self.invFact[i-1] = (self.invFact[i] * i) % self.MOD

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        self.factorial(n)
        self.inverseFactorial(n)

        comb = (self.fact[n-1] * self.invFact[n-k-1]) % self.MOD * self.invFact[k] % self.MOD
        nums = m * self.binExp(m-1, n-k-1)

        return (comb * nums) % self.MOD

'''

111222333
n = 9
m = 3
k = 6

totalPairs = n - 1
notEqual = n - 1 - k
groups = (n - k - 1) + 1 = n-k

combinations = totalPairs! / notEqual! * k!

numbers = m * (m-1)**(groups-1)

total = combinations * numbers

'''

def test ():
    params = [
        {
            'input': [3, 2, 1],
            'output': 4,
        },
        {
            'input': [4, 2, 2],
            'output': 6,
        },
        {
            'input': [5, 2, 0],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        n, m, k = param['input']
        result = solution.countGoodArrays(n, m, k)
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
