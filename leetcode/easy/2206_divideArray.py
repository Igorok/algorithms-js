from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numsSum = defaultdict(int)

        for num in nums:
            numsSum[num] += 1

        for s in numsSum.values():
            if s % 2 == 1:
                return False

        return True


def test ():
    params = [
        {
            'input': [3,2,3,2,2,2],
            'output': True,
        },
        {
            'input': [1,2,3,4],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.divideArray(nums)
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
