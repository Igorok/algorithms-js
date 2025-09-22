from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution_0:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(num1, num2):
            num1, num2 = sorted([num1, num2])
            remainder = num2 % num1
            if remainder == 0:
                return num1
            return gcd(remainder, num1)

        def lcm(num1, num2):
            return int(num1 * num2 / gcd(num1, num2))

        def rec(arr, id):
            stack = []
            found = False

            rng = range(len(arr))
            if id % 2 == 0:
                rng = reversed(rng)

            for i in rng:
                if len(stack) == 0:
                    stack.append(arr[i])
                    continue

                g = gcd(stack[-1], arr[i])
                if g == 1:
                    stack.append(arr[i])
                    continue

                l = int(stack[-1] * arr[i] / g)
                stack.pop()
                stack.append(l)
                found = True

            if id % 2 == 0:
                stack = list(reversed(stack))

            return rec(stack, id+1) if found else stack

        return rec(nums, 0)

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        cache = {}
        def gcd(num1, num2):
            num1, num2 = sorted([num1, num2])
            if ((num1, num2) in cache):
                return cache[(num1, num2)]

            remainder = num2 % num1
            if remainder == 0:
                return num1

            cache[(num1, num2)] = gcd(remainder, num1)
            return cache[(num1, num2)]

        def lcm(num1, num2):
            return int(num1 * num2 / gcd(num1, num2))

        stack = []

        for i in range(len(nums)):
            stack.append(nums[i])

            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                g = gcd(stack[-1], stack[-2])
                l = int(stack[-1] * stack[-2] / g)
                stack.pop()
                stack.pop()
                stack.append(l)

        return stack

'''

'''


def test ():
    params = [
        {
            'input': [3,2,3,2,3,2,3,2,3,2,3,2,3,6,6],
            'output': [6],
        },
        {
            'input': [287,41,49,287,899,23,23,20677,5,825],
            'output': [2009,20677,825],
        },
        {
            'input': [6,4,3,2,7,6,2],
            'output': [12,7,6],
        },
        {
            'input': [2,2,1,1,3,3,3],
            'output': [2,1,1,3],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.replaceNonCoprimes(nums)
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
