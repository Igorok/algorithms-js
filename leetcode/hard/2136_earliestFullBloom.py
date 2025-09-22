from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        flowers = [[plantTime[i], growTime[i]] for i in range(n)]
        flowers.sort(key=lambda x: -x[1])

        plant = 0
        total = 0

        for i in range(n):
            pl, gr = flowers[i]
            plant += pl
            total = max(total, plant+gr)

        return total

'''
'input': [[1,4,3], [2,3,1]],

----0 1 2 3 4 5 6 7 8 9 10
1,2 p g g b
4,3 - p p p p g g g b
3,1 - - - - - p p p g b

----0 1 2 3 4 5 6 7 8 9 10
4,3 p p p p g g g b
1,2 - - - - - - p g g b
3,1 - - - - p p - p g b

3+1+4 = 8
1+2+3 = 3

---

plantTime = [1,2,3,2], growTime = [2,1,2,1]

1,2




'''



def test ():
    params = [
        {
            'input': [[1,4,3], [2,3,1]],
            'output': 9,
        },
        {
            'input': [[1,2,3,2], [2,1,2,1]],
            'output': 9,
        },
        {
            'input': [[1], [1]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        plantTime, growTime = param['input']
        result = solution.earliestFullBloom(plantTime, growTime)
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
