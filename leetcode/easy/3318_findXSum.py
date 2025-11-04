from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        length = n - k + 1
        countOfNums = {}

        def getSum():
            data = [(k, countOfNums[k]) for k in countOfNums]
            data.sort(key=lambda x: [-x[1], -x[0]])
            r = 0
            for i in range(min(x, len(data))):
                r += data[i][0] * data[i][1]
            return r

        for i in range(k):
            num = nums[i]
            countOfNums[num] = countOfNums.get(num, 0) + 1

        res = [getSum()]

        for i in range(k, n):
            num = nums[i]
            countOfNums[num] = countOfNums.get(num, 0) + 1
            prevId = i - k
            num = nums[prevId]

            if countOfNums[num] == 1:
                del countOfNums[num]
            else:
                countOfNums[num] -= 1

            res.append(getSum())


        return res

def test ():
    params = [
        {
            'input': [[1,1,2,2,3,4,2,3], 6, 2],
            'output': [6,10,12],
        },
        {
            'input': [[3,8,7,8,7,5], 2, 2],
            'output': [11,15,15,15,12],
        },
    ]
    solution = Solution()

    for param in params:
        nums, k, x = param['input']
        result = solution.findXSum(nums, k, x)
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
