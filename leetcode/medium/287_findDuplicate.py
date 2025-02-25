from typing import List
import json
from collections import deque

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                break

        return slow

def test ():
    params = [
        {
            'input': [1,3,4,2,2],
            'output': 2,
        },
        {
            'input': [3,1,3,4,2],
            'output': 3,
        },
        {
            'input': [3,3,3,3,3],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findDuplicate(param['input'])
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
