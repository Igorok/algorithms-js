from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        numsHeap = []
        for num in nums:
            count[num] += 1

        for key in count:
            heapq.heappush(numsHeap, (-count[key], key))

        res = []
        for i in range(k):
            count, val = heapq.heappop(numsHeap)
            res.append(val)

        return res


def test ():
    params = [
        {
            'input': [[5,3,1,1,1,3,73,1], 2],
            'output': [1,3],
        },
        {
            'input': [[1,1,1,2,2,3], 2],
            'output': [1,2],
        },
        {
            'input': [[1], 1],
            'output': [1],
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.topKFrequent(nums, k)
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
