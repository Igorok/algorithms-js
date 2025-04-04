from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        n = len(weights)
        arr = [weights[i] + weights[i+1] for i in range(n-1)]
        arr.sort()

        common = weights[0] + weights[n-1]
        minSum = common + sum(arr[:k-1])
        maxSum = common + sum(arr[n-k:])

        return maxSum - minSum

'''

2
1,3,5,1
2+4
4+6


1,2,1,2,1
241 = 7
331=7

1 1 5 6 1
2 2 = 4
6 7 = 13

---

[1, 1, 5, 6, 1, 1, 1, 5, 6, 1], 3
2 2 2 = 6
6 11 7 = 24
18

1, 1, 5, 6, 1, 1, 1, 5, 6, 1

2 6 11 7 2 2 6 11 7

(1+1) + 2 + 2 + 2 = 8
(1+1) + 11 + 11 + 7 =

(l[1]+r[n]) + (r[1]+l[2]) + ... + (r[n-1] + l[n])



'''

def test ():
    params = [
        {
            'input': [[1,3,5,1], 2],
            'output': 4,
        },
        {
            'input': [[1, 3], 2],
            'output': 0,
        },
        {
            'input': [[1,2,1,2,1], 3],
            'output': 0,
        },
        {
            'input': [[1, 1, 5, 6, 1], 2],
            'output': 9,
        },
        {
            'input': [[1, 1, 5, 6, 1, 1, 1, 5, 6, 1], 3],
            'output': 18,
        },
        {
            'input': [[1, 1, 5, 6, 1, 1, 1, 5, 6, 1], 4],
            'output': 23,
        },
    ]
    solution = Solution()

    for param in params:
        weights, k = param['input']
        result = solution.putMarbles(weights, k)
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
