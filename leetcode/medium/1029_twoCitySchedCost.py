from typing import List
import json
from collections import deque
import heapq


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        halfN = N // 2
        data = sorted(costs, key=lambda x: x[0]-x[-1])

        res= 0
        for i in range(N):
            res += data[i][0] if i < halfN else data[i][1]

        return res

'''

[1,2], [2,3], [3,10],[4,11]
-1, -1, -7, -7
-7,-7,-1,-1

---

[2, 1], [3, 2], [10, 3], [11, 4]
1, 1, 7, 7



'''




def test ():
    params = [
        {
            'input': [[10,20],[30,200],[400,50],[30,20]],
            'output': 110,
        },
        {
            'input': [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]],
            'output': 1859,
        },
        {
            'input': [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]],
            'output': 3086,
        },
    ]
    solution = Solution()

    for param in params:
        costs = param['input']
        result = solution.twoCitySchedCost(costs)
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
