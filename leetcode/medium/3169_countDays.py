from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def countDays_0(self, days: int, meetings: List[List[int]]) -> int:
        openArr = [0] * (days + 1)
        closeArr = [0] * (days + 1)
        for s, e in meetings:
            openArr[s] += 1
            closeArr[e] += 1

        res = 0
        opened = 0
        for i in range(1, days+1):
            opened += openArr[i]
            opened -= closeArr[i]
            if opened == 0 and openArr[i] == 0 and closeArr[i] == 0:
                res += 1

        return res



    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])

        res = 0
        openDay = 0
        closeDay = 0

        for s, e in meetings:
            if s > closeDay + 1:
                res += s - closeDay - 1
            closeDay = max(closeDay, e)

        if days > closeDay:
            res += days - closeDay

        return res


'''

[0,0],[1,6],[2,3],[3,5],[8,8],[9,9]

close = 8
open = 8

---

[5, [[1, 3], [2, 4]]]






'''

def test ():
    params = [
        {
            'input': [8, [[1,6],[2,3],[3,5],[8,8]]],
            'output': 1,
        },
        {
            'input': [8, [[2,3],[3,5],[8,8]]],
            'output': 3,
        },
        {
            'input': [10, [[5,7],[1,3],[9,10]]],
            'output': 2,
        },
        {
            'input': [5, [[2,4],[1,3]]],
            'output': 1,
        },
        {
            'input': [6, [[1,6]]],
            'output': 0,
        },
        {
            'input': [1000000000, [[1,1000000000]]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        days, meetings = param['input']
        result = solution.countDays(days, meetings)
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
