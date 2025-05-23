from typing import List
import json
from collections import deque, defaultdict
import math
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        qArray = sorted(queries, key=lambda x: x[0])
        maxAvailableHeap = []
        minUsedHeap = []
        qId = 0
        qUsed = 0

        n = len(nums)
        m = len(qArray)

        for i in range(n):
            while qId < m and qArray[qId][0] == i:
                heapq.heappush(maxAvailableHeap, -qArray[qId][1])
                qId += 1

            count = nums[i]
            count -= len(minUsedHeap)

            while count > 0 and maxAvailableHeap:
                qEnd = -heapq.heappop(maxAvailableHeap)
                if qEnd < i:
                    continue
                heapq.heappush(minUsedHeap, qEnd)
                count -= 1
                qUsed += 1

            if count > 0:
                return -1

            while minUsedHeap and minUsedHeap[0] == i:
                heapq.heappop(minUsedHeap)

        return m - qUsed



def test ():
    params = [
        {
            'input': [
                [0,0,3],
                [[0,2],[1,1],[0,0],[0,0]],
            ],
            'output': -1,
        },
        {
            'input': [[1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]],
            'output': 2,
        },
        {
            'input': [[2,0,2], [[0,2],[0,2],[1,1]]],
            'output': 1,
        },
        {
            'input': [[1,2,3,4], [[0,3]]],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        nums, queries = param['input']
        result = solution.maxRemoval(nums, queries)
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
