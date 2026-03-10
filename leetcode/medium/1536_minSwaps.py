from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        data = []
        for r in range(N):
            cnt = 0
            for c in range(N-1,-1,-1):
                if grid[r][c] == 1:
                    break
                cnt += 1
            data.append(cnt)

        res = 0
        for r in range(N-1):
            required = N - r - 1
            if data[r] >= required:
                continue

            steps = 0
            for i in range(r+1, N):
                if data[i] < required:
                    continue
                steps = i - r
                res += steps

                top = data[:r]
                middle = data[r:i]
                bottom = data[i+1:]

                top.append(data[i])

                data = top + middle + bottom
                break

            if steps == 0:
                return -1




        return res


'''

[
[1,0,0,0],
[1,1,1,1],
[1,0,0,0],
[1,0,0,0]
]

---

[
[1,0,0,0],
[1,1,1,1],
[1,0,0,0],
[1,0,0,0]
]



'''


def test ():
    params = [
        {
            'input': [[0,0,1],[1,1,0],[1,0,0]],
            'output': 3,
        },
        {
            'input': [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],
            'output': -1,
        },
        {
            'input': [[1,0,0],[1,1,0],[1,1,1]],
            'output': 0,
        },
        {
            'input': [[1,1,1,1,1],[1,0,0,0,0],[1,1,1,0,0],[1,1,0,0,0],[1,1,1,1,0]],
            'output': 5,
        },
        {
            'input': [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.minSwaps(grid)
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
