from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        m = 7+10e8
        curr_sum = 0
        even_sum = 1
        odd_sum = 0
        total = 0

        for num in arr:
            curr_sum += num

            if curr_sum % 2 == 1:
                odd_sum += 1
                total += even_sum
                total %= m
            else:
                even_sum += 1
                total += odd_sum
                total %= m


        return int(total)

'''
sum, even sum, odd sum
1;  1, 1, 1;    1
1 1;    2, 2, 1;    2
1 1 1;  3, 2, 2;    4
1 1 1 2;    5, 2, 3;   6
1 1 1 2 2;  7, 2, 4;    8
1 1 1 2 2 1;    8, 3, 4;    12


'''


def test ():
    params = [
        {
            'input': [1,3,5],
            'output': 4,
        },
        {
            'input': [2,4,6],
            'output': 0,
        },
        {
            'input': [1,2,3,4,5,6,7],
            'output': 16,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.numOfSubarrays(nums)
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
