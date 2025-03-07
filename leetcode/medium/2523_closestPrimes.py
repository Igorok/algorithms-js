from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def closestPrimes_0(self, left: int, right: int) -> List[int]:
        res = [-1, -1]
        primeNumbers = []

        def isPrimeNumber(num):
            if num <= 3:
                return True

            n = math.ceil(num ** 0.5)

            for i in range(2, n+1):
                if num % i == 0:
                    return False

            return True

        for i in range(left, right+1):
            if isPrimeNumber(i):
                primeNumbers.append(i)
                if res[0] == -1:
                    res[0] = i
                    continue
                if res[1] == -1:
                    res[1] = i
                    continue
                diff = primeNumbers[-1] - primeNumbers[-2]
                if diff < res[1] - res[0]:
                    res = [primeNumbers[-2], primeNumbers[-1]]
                if res[1] - res[0] == 1 or res[1] - res[0] == 2:
                    return res


        return [-1, -1] if res[1] == -1 else res

    def closestPrimes(self, left: int, right: int) -> List[int]:
        def getSieve():
            primeNumbers = []
            sieve = [True] * (right+1)
            sieve[0] = False
            sieve[1] = False
            n = math.ceil(right ** (1/2))

            for i in range(2, n+1):
                if not sieve[i]:
                    continue
                for j in range(i*i, right+1, i):
                    if j % i == 0:
                        sieve[j] = False

            return sieve

        res = [-1, -1]
        sieve = getSieve()
        primeNumbers = []

        for i in range(left, right+1):
            if not sieve[i]:
                continue

            primeNumbers.append(i)
            if res[0] == -1:
                res[0] = i
                continue
            if res[1] == -1:
                res[1] = i
                continue

            if len(primeNumbers) > 1 and primeNumbers[-1] - primeNumbers[-2] < res[1] - res[0]:
                res = [primeNumbers[-2], primeNumbers[-1]]

            if (res[1] - res[0] == 1) or (res[1] - res[0] == 2):
                return res


        return [-1, -1] if res[1] == -1 else res



def test ():
    params = [
        {
            'input': [255322, 929209],
            'output': [255467, 255469],
        },
        {
            'input': [10, 19],
            'output': [11,13],
        },
        {
            'input': [4, 6],
            'output': [-1,-1],
        },
        {
            'input': [19, 31],
            'output': [29, 31],
        },

    ]
    solution = Solution()

    for param in params:
        left, right = param['input']
        result = solution.closestPrimes(left, right)
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
