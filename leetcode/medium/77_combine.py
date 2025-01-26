from typing import List
from json import dumps
from collections import deque

class Solution:
    def combine_0(self, n: int, k: int) -> List[List[int]]:
        res = []
        def rec(arr):
            if len(arr) == k:
                res.append(arr)
                return

            num = 0 if len(arr) == 0 else arr[-1]

            for i in range(num+1, n + 1):
                a = arr.copy()
                a.append(i)
                rec(a)

        rec([])

        return res


'''

1 2 3 4
1 2
1 3
1 4
  2 3
  2 4
    3 4


'''

def test ():
    params = [
        {
            'input': [4, 2],
            'output': [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]],
        },
        {
            'input': [1, 1],
            'output': [[1]],
        },
        {
            'input': [2, 1],
            'output': [[1],[2]],
        },
    ]
    solution = Solution()

    for param in params:
        n, k = param['input']
        result = solution.combine(n, k)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
