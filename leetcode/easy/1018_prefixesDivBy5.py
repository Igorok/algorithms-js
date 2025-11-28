from typing import List
import json
from collections import deque
import heapq

class Solution_0:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        N = len(nums)
        remainders = [16, 32, 64, 128]

        acc = nums[0]
        res = [False] * N
        res[0] = acc == 0

        for i in range(1, N):
            if nums[i] == 0:
                acc += 0
            else:
                acc += remainders[i % 4]

            # if i > 2:
            #     acc += 5

            acc %= 5
            res[i] = (acc == 0)


        return res


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        N = len(nums)
        res = [False] * N
        acc = 0

        for i in range(0, N):
            acc = acc << 1
            acc += nums[i]
            acc %= 5
            res[i] = acc == 0


        return res




def test ():
    params = [
        {
            'input': [0,1,1],
            'output': [True,False,False],
        },
        {
            'input': [1,1,1],
            'output': [False,False,False],
        },
        {
            'input': [0,1,1,1,1,1],
            'output': [True,False,False,False,True,False],
        },
        {
            'input': [1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0],
            'output': [False,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.prefixesDivBy5(nums)
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
