from typing import List
import json
from collections import deque

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        N = len(tasks)
        memo = {}
        day = 1

        for i in range(N):
            task = tasks[i]

            if (task not in memo) or (day - memo[task] >= space+1):
                memo[task] = day
            else:
                day = memo[task] + space + 1
                memo[task] = day

            if i != N-1:
                day += 1

        return day

'''
5 - 1
8 - 2
'''

def test ():
    params = [
        {
            'input': [[1,2,1,2,3,1], 3],
            'output': 9,
        },
        {
            'input': [[5,8,8,5], 2],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        tasks, space = param['input']
        result = solution.taskSchedulerII(tasks, space)
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
