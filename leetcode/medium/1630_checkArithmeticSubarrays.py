from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        res = [True] * n

        for i in range(len(l)):
            left = l[i]
            right = r[i]

            if right - left + 1 < 3:
                continue

            sub = sorted(nums[left:right+1])
            diff = sub[1] - sub[0]
            wrong = False

            for j in range(2, len(sub)):
                if sub[j] - sub[j-1] != diff:
                    res[i] = False
                    break

        return res

'''

500 * (Math.log2(500)*500 + 500) = 2491446.071165522
2_491_446

[4,6,5,9,3,7]

'''

def test ():
    params = [
        {
            'input': [[4,6,5,9,3,7], [0,0,2], [2,3,5]],
            'output': [True,False,True],
        },
        {
            'input': [[-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]],
            'output': [False,True,False,False,True,True],
        },
    ]
    solution = Solution()

    for param in params:
        nums, l, r = param['input']

        result = solution.checkArithmeticSubarrays(nums, l, r)

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
