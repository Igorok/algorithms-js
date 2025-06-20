from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxValues = []
        minValues = []
        counter = defaultdict(int)

        res = 0
        left = 0
        for right in range(len(nums)):
            heapq.heappush(maxValues, -nums[right])
            heapq.heappush(minValues, nums[right])
            counter[nums[right]] += 1

            while (-maxValues[0]) - minValues[0] > limit:
                counter[nums[left]] -= 1

                if -maxValues[0] == nums[left]:
                    heapq.heappop(maxValues)

                if minValues[0] == nums[left]:
                    heapq.heappop(minValues)

                while counter[-maxValues[0]] == 0:
                    heapq.heappop(maxValues)

                while counter[minValues[0]] == 0:
                    heapq.heappop(minValues)

                left += 1

            r = right - left + 1
            res = max(res, r)


        return res

def test ():
    params = [
        {
            'input': [[8,2,4,7], 4],
            'output': 2,
        },
        {
            'input': [[10,1,2,4,7,2], 5],
            'output': 4,
        },
        {
            'input': [[4,2,2,2,4,4,2,2], 0],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        nums, limit = param['input']
        result = solution.longestSubarray(nums, limit)
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
