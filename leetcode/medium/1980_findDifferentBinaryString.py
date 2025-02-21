from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def findDifferentBinaryString_0(self, nums: List[str]) -> str:
        n = len(nums[0])
        unique = set(nums)

        def rec(text):
            if len(text) == n:
                if not text in unique:
                    return text
                else:
                    return ''

            t = rec(text + '0')
            if t:
                return t

            return rec(text + '1')

        return rec('')

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        unique = set(nums)

        for i in range(2**n):
            b = bin(i)[2:]
            diff = n - len(b)
            if diff:
                b += '0'*diff
            print('b', b)

            if not b in unique:
                return b

        return ''


def test ():
    params = [
        {
            'input': ["01","10"],
            'output': '11',
        },
        {
            'input': ["00","01"],
            'output': '11',
        },
        {
            'input': ["111","011","001"],
            'output': '101',
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.findDifferentBinaryString(nums)
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
