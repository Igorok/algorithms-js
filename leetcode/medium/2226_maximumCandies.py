from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sumOfCandy = sum(candies)
        if sumOfCandy < k:
            return 0

        def canDivide(num):
            count = 0
            for pile in candies:
                count += pile // num
                if count >= k:
                    return True

            return count >= k

        end = sumOfCandy // k
        start = 1
        res = 0

        while start <= end:
            m = (start + end) // 2
            if canDivide(m):
                res = m
                start = m + 1
            else:
                end = m - 1

        return res


def test ():
    params = [
        {
            'input': [[5,8,6], 3],
            'output': 5,
        },
        {
            'input': [[2,5], 11],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        candies, k = param['input']
        result = solution.maximumCandies(candies, k)
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
