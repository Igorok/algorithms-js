from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        nums[0] -= k

        unique = set([nums[0]])

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                diff = nums[i] - nums[i-1]
                if diff - 1 > k:
                    diff = k
                else:
                    diff -= 1
                nums[i] -= diff
            else:
                diff = nums[i-1] - nums[i]
                diff = diff + 1
                if diff > k:
                    diff = k
                nums[i] += diff


            unique.add(nums[i])

        return len(unique)

'''
[[1,2,2,3,3,4], 2],
1,  2, 2, 3, 3, 4
-1, 0, 1, 2, 3, 4

---
1
1,2,2,2,3,3,3,
0,1,2,3,4,4,4,


'''

def test ():
    params = [
        {
            'input': [[1,1,1,1,1,1,1,1,5,5,5], 3],
            'output': 10,
        },
        {
            'input': [[1,2,2,3,3,4], 2],
            'output': 6,
        },
        {
            'input': [[4,4,4,4], 1],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.maxDistinctElements(nums, k)
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
