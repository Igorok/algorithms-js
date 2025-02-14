import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        numsQueue = nums
        heapq.heapify(numsQueue)

        while len(numsQueue) > 1:
            if numsQueue[0] >= k:
                return res

            x = heapq.heappop(numsQueue)
            y = heapq.heappop(numsQueue)
            z = min(x, y) * 2 + max(x, y)
            heapq.heappush(numsQueue, z)

            res += 1

        return res

def test ():
    params = [
        {
            'input': [[2,11,10,1,3], 10],
            'output': 2,
        },
        {
            'input': [[1,1,2,4,9], 20],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.minOperations(nums, k)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
