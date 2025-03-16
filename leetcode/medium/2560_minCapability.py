from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minCap = float('inf')
        maxCap = -1
        for num in nums:
            minCap = min(minCap, num)
            maxCap = max(maxCap, num)



        def checkCapability(num):
            nonlocal nums, k, n

            prev = -2
            count = 0

            for i in range(n):
                if nums[i] <= num and prev+1 < i:
                    count += 1
                    prev = i
                    if count == k:
                        return True

            return False



        start = minCap
        end = maxCap
        res = maxCap
        while start <= end:
            m = (start + end) // 2
            if checkCapability(m):
                res = m
                end = m - 1
            else:
                start = m + 1

        return res


def test ():
    params = [
        {
            'input': [[2,3,5,9], 2],
            'output': 5,
        },
        {
            'input': [[2,7,9,3,1], 2],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.minCapability(nums, k)
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
